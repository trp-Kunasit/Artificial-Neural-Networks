"""
Teerapong Kunasit
Problem 4: Climate Model - Energy Balance Model Calculator
"""

def calculate_temperature(solar_heat: float, albedo: float, emissivity: float) -> float:

    STEFAN_BOLTZMANN = 5.67e-8 
    
    numerator = (1 - albedo) * solar_heat
    denominator = emissivity * STEFAN_BOLTZMANN
    
    temperature = (numerator / denominator) ** 0.25
    
    return temperature

def main():
    try:
        solar_heat = float(input("S: "))
        albedo = float(input("a: "))
        emissivity = float(input("e: "))
        
        
        if solar_heat <= 0 or albedo < 0 or albedo >= 1 or emissivity <= 0:
            raise ValueError("Invalid input values")
            
        temperature = calculate_temperature(solar_heat, albedo, emissivity)
        print(f"T= {temperature:.2f}")
        
    except ValueError as e:
        if str(e) == "Invalid input values":
            print("Error: Please enter valid values")
        else:
            print("Error: Please enter numeric values")

if __name__ == "__main__":
    main()