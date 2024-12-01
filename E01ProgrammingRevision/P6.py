"""
Teerapong Kunasit
Problem 6: Base-3 Stone Code Calculator
"""

def base3_to_decimal(stone_code: str) -> int:
    if not (len(stone_code) == 3 and all(c in '012' for c in stone_code)):
        raise ValueError("Stone code must be 3 digits of 0, 1, or 2")
        
    a = int(stone_code[0]) * 9  
    b = int(stone_code[1]) * 3  
    c = int(stone_code[2]) * 1  
    
    return a + b + c

def main():
    try:
        stone_code = input("Stones: ")
        lapses = base3_to_decimal(stone_code)
        print(f"Lapses= {lapses}")
        
    except ValueError:
        print("Error: Please enter a valid 3-digit stone code (000-222)")

if __name__ == "__main__":
    main()