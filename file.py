import sys

def process_file(filename: str):
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                try:
                    #make the line into two seperate float values
                    values = line.split()
                    if len(values) != 2:
                        print(f"Error: Line '{line}' does not contain exactly two values.")
                        continue

                    #calc the floats into a sum
                    num1, num2 = float(values[0]), float(values[1])
                    print(f"The sum of {num1} and {num2} is {num1 + num2}")

                except ValueError:
                    print(f"Error: Line '{line}' does not contain valid float values.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' could not be opened.")
        sys.exit(1)  #end program with error code


def main():
    if len(sys.argv) != 2:
        print("Error: Please provide a filename as a command-line argument.")
        sys.exit(1)

    filename = sys.argv[1]
    process_file(filename)

if __name__ == "__main__":
    main()

    #OUTPUT TEST 1
    # The sum of 3.2 and 4.5 is 7.7
    # The sum of 1.5 and 2.3 is 3.8
    # Error: Line 'hello 3.0' does not contain valid float values.
    # Error: Line '4.0 abc' does not contain valid float values.
    # The sum of 5.5 and 6.1 is 11.6

    #OUTPUT TEST 2
    # The sum of 3.2 and 5.0 is 8.2
    # The sum of 1.7 and 2.3 is 4.0
    # Error: Line 'hello hello world' does not contain exactly two values.
    # The sum of 4.0 and 11.5 is 15.5
    # Error: Line '5.5 nope' does not contain valid float values.

