# Rectangle Area Calculator

# Function to calculate the area of a rectangle
def calculate_area(length, width):
    return length * width

# Main function to execute the program
def main():
    # Get user input
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Calculate area
    area = calculate_area(length, width)

    # Display the result
    print(f"The area of the rectangle is: {area}")

# Entry point of the program
if __name__ == "__main__":
    main()