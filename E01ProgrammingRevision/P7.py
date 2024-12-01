"""
Teerapong Kunasit
Problem 7: SIR Model Disease Spread Calculator
"""
from dataclasses import dataclass
from typing import TextIO

@dataclass
class SIRState:
    S: float  
    I: float  
    R: float  
    period: int = 0

class SIRModel:
    def __init__(self, initial_state: SIRState, contact_rate: float, removal_rate: float):
        self.state = initial_state
        self.c = contact_rate
        self.r = removal_rate
    
    def step(self) -> SIRState:
        dS = -self.c * self.state.S * self.state.I
        dI = self.c * self.state.S * self.state.I - self.r * self.state.I
        dR = self.r * self.state.I
        
        self.state = SIRState(
            S=self.state.S + dS,
            I=self.state.I + dI,
            R=self.state.R + dR,
            period=self.state.period + 1
        )
        return self.state
    
    def is_spreading(self) -> bool:
        return self.c * self.state.S > self.r

def write_state(file: TextIO, state: SIRState):
    file.write(f"Period {state.period:6d}")
    file.write(f"  S={state.S:10.2f}")
    file.write(f"  I={state.I:10.2f}")
    file.write(f"  R={state.R:10.2f}\n")

def main():
    try:
        S0, I0, R0 = map(float, input("Initial S, I, R: ").split())
        c, r = map(float, input("c, r: ").split())
        periods = int(input("periods: "))
        
        if any(x < 0 for x in [S0, I0, R0, c, r, periods]):
            raise ValueError("All values must be non-negative")
        
        initial_state = SIRState(S0, I0, R0)
        model = SIRModel(initial_state, c, r)
        
        with open("epidemic.txt", "w") as f:
            write_state(f, model.state)
            for _ in range(periods):
                state = model.step()
                write_state(f, state)

        if model.is_spreading():
            print("--> It is spreading!")
        else:
            print("--> It is contained!")
            
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()