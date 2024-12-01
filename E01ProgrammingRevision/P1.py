#Teerapong Kunasit

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
    
    observationCodes = str(input("observe:")).strip()
    if observationCodes in directions:
        facing = directions[observationCodes]
        print(f"facing {facing}")
    else:
        print("Invalid observation code!")
    
if __name__ == "__main__":
    main()