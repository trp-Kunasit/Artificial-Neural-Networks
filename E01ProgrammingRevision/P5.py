"""
Teerapong Kunasit
Problem 5: Old-time Sailor - Longitude Calculator
"""

def parse_time(time_str: str) -> int:

    time_part = time_str[:-1]  
    meridiem = time_str[-1].lower()
    
    hours, minutes = map(int, time_part.split(':'))
    
    if meridiem == 'p' and hours != 12:
        hours += 12
    elif meridiem == 'a' and hours == 12:
        hours = 0
        
    return hours * 60 + minutes

def calculate_longitude(minutes_since_midnight: int) -> tuple[float, str]:
    
    NOON_MINUTES = 12 * 60  
    
    
    time_diff = minutes_since_midnight - NOON_MINUTES
    
    
    longitude = abs(time_diff / 4.0)
    
    
    if minutes_since_midnight == NOON_MINUTES:
        return 0.0, ''
    elif minutes_since_midnight < NOON_MINUTES:
        return longitude, 'E'
    else:
        return longitude, 'W'

def main():
    try:
        gmt = input("GMT: ")
        
        minutes = parse_time(gmt)
        
        longitude, direction = calculate_longitude(minutes)
        
        if direction:
            print(f"longitude= {longitude:.2f} {direction}")
        else:
            print(f"longitude= {longitude:.2f}")
            
    except (ValueError, IndexError):
        print("Error: Invalid time format. Please use HH:MMa/p")

if __name__ == "__main__":
    main()