def calculate_job_compensation():
    """
    Calculates the total job compensation based on salary, equity, bonus, and other perks.
    """
    try:
        print("=== Job Compensation Calculator ===")
        
        # Gather inputs from the user
        salary = float(input("Enter the annual base salary (in your local currency): "))
        equity_value = float(input("Enter the annualized equity value (in your local currency): "))
        performance_bonus = float(input("Enter the annual performance bonus (in your local currency): "))
        other_perks = float(input("Enter the value of other perks (in your local currency): "))
        
        # Calculate the total compensation
        total_compensation = salary + equity_value + performance_bonus + other_perks
        
        # Display the results
        print("\n--- Breakdown ---")
        print(f"Base Salary: {salary:.2f}")
        print(f"Equity Value: {equity_value:.2f}")
        print(f"Performance Bonus: {performance_bonus:.2f}")
        print(f"Other Perks: {other_perks:.2f}")
        print("\n--- Total Compensation ---")
        print(f"Total Annual Compensation: {total_compensation:.2f}")
    
    except ValueError:
        print("Error: Please enter valid numbers.")
        
# Run the calculator
calculate_job_compensation()
