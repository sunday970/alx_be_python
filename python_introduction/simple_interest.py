# Simple Interest Calculator

# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# Main function to execute the program
def main():
    # Get user input
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in %): "))
    time = float(input("Enter the time period in years: "))

    # Calculate simple interest
    interest = calculate_simple_interest(principal, rate, time)

    # Display the result
    print(f"The simple interest is: {interest}")

# Entry point of the program
if __name__ == "__main__":
    main()


