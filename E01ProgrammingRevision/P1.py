"""
Teerapong Kunasit
Problem 1: Direction Mapper
"""

def main():
    directions = {
        "U": "east",
        "D": "west", 
        "L": "north",
        "R": "south",
        "UL": "north-east",
        "UR": "south-east", 
        "DL": "north-west",
        "DR": "south-west"
    }
    
    observation = input("observe: ").strip()
    if observation in directions:
        print(f"facing {directions[observation]}")
    else:
        print("Invalid observation code!")

if __name__ == "__main__":
    main()