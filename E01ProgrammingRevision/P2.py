#Teerapong Kunasit

def main():
    xbar = 0  
    n = 0     
    
    while True:
        x = float(input(f"x{n+1}: "))
        if x < 0:  
            if n > 0:  
                xbar = (xbar * n + x) / (n + 1)  
            break
        n += 1  
        xbar = (xbar * (n - 1) + x) / n
        print(f"mean = {xbar:.4f}")
        
    print(f"mean = {xbar:.4f}")
    
if __name__ == "__main__":
    main()