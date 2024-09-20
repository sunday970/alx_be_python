# finance_calculator.py

def main():
    # User Input for Financial Details
    monthly_income = float(input("Enter your monthly income: "))
    monthly_expenses = float(input("Enter your total monthly expenses: "))

    # Calculate Monthly Savings
    monthly_savings = monthly_income - monthly_expenses

    # Project Annual Savings
    annual_interest_rate = 0.05  # 5% interest
    projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

    # Output Results
    print(f"\nYour monthly savings: ${monthly_savings:.2f}")
    print(f"Projected annual savings after including interest: ${projected_savings:.2f}")

if __name__ == "__main__":
    main()