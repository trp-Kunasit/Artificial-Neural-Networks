"""
Teerapong Kunasit
Problem 2: Online Averaging Calculator
"""

def main():
    numbers = []
    count = 1
    
    try:
        while True:
            print(f"x{count}: ", end='')
            line = input().strip()
            
            if not line:  
                continue
                
            number = float(line)
            
            numbers.append(number)
            mean = sum(numbers) / len(numbers)
            print(f"mean={mean:.4f}")
            
            if number < 0:
                break
                
            count += 1
            
    except EOFError:
        if numbers:  
            mean = sum(numbers) / len(numbers)
            print(f"mean={mean:.4f}")

if __name__ == "__main__":
    main()