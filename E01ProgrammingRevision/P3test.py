def extract_eeg_sequence(file_name, trial_number, sensor_position):
    try:
        with open(file_name, 'r') as file:
            sequence = []  # List to store the EEG sequence
            target_series = f"{trial_number} {sensor_position}"
            
            for line in file:
                line = line.strip()  # Remove any extra spaces or newlines
                # Skip metadata lines
                if line.startswith('#'):
                    continue
                
                # Split the data line into parts
                parts = line.split()
                
                # Check if the line matches the desired trial and sensor position
                if f"{parts[0]} {parts[1]}" == target_series:
                    # Append the EEG value (last column) to the sequence
                    sequence.append(float(parts[-1]))
            
            # Return the extracted sequence
            return sequence
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Main program
def main():
    # Get user inputs
    file_name = input("File: ").strip()
    text_input = input("Series: ").split()
    trial_number = text_input[0]
    sensor_position = text_input[1]
    # Extract EEG sequence
    sequence = extract_eeg_sequence(file_name, trial_number, sensor_position)
    
    # Display the result
    if sequence is not None:
        # print(f"Series: {trial_number} {sensor_position}")
        print(sequence)

if __name__ == "__main__":
    main()