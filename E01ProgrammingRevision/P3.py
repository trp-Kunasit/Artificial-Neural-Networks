"""
Teerapong Kunasit
Problem: 3 EEG sequence

"""


def main():
    filename = input("Enter the filename: ")
    series_input = input("Enter the series (e.g., 'Series: 0 FP2'): ")

    try:

        split_SI = series_input.split()
        if len(split_SI) != 2:
            raise ValueError(
                "Invalid format. Please use '[Trial Number] [Sensor Position]'"
            )

        trial_number = split_SI[0]
        sensor_position = split_SI[1]

        with open(filename, "r") as file:
            result = []
            for line in file:
                if line.startswith("#"):
                    continue

                split_SI = line.split()
                if len(split_SI) < 4:
                    continue

                trial, sensor, _, value = split_SI
                if trial == trial_number and sensor == sensor_position:
                    if len(result) < 4:
                        result.append(float(value))
                    else:
                        break

            if result:
                print(f"{result}")
            else:
                print("No data found matching the criteria.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


if __name__ == "__main__":
    main()