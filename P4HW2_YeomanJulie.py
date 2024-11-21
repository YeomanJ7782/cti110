# Julie Yeoman
# P4HW2
# 11/10/2024
# CTI-110
# Employee Pay Calculator with Multiple Employees

'''
# Pseudocode :
# 1. Initialize total variables for overtime, regular pay, and gross pay
# 2. Initialize employee counter
# 3. Display program title
# 4. Enter loop that continues until user enters "Done":
#    a. Get employee name
#    b. If name is "Done" (case-insensitive), exit loop
#    c. Get hours worked and pay rate
#    d. Calculate payments:
#       - Check if hours > 40 for overtime
#       - If overtime:
#         * Calculate overtime hours (hours - 40)
#         * Calculate overtime pay (overtime hours * pay rate * 1.5)
#         * Calculate regular pay (40 * pay rate)
#       - If no overtime:
#         * Set overtime hours and pay to 0
#         * Calculate regular pay (hours * pay rate)
#       - Calculate gross pay (regular pay + overtime pay)
#    e. Add to running totals:
#       - Add overtime pay to overtime total
#       - Add regular pay to regular total
#       - Add gross pay to gross total
#    f. Increment employee counter
#    g. Display individual employee results
# 5. After loop ends, display:
#    - Total number of employees entered
#    - Total amount paid for overtime
#    - Total amount paid for regular hours
#    - Total amount paid in gross
'''

# Initialize totals
total_overtime = 0
total_regular = 0
total_gross = 0
employee_count = 0

print("Employee Pay Calculator")
print("-" * 50)

while True:
    # Get employee name
    employee_name = input("\nEnter employee's name or 'Done' to terminate: ").strip()
    
    # Check for termination condition
    if employee_name.lower() == 'done':
        break
        
    # Get hours and pay rate
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
    
    # Calculate overtime
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * pay_rate * 1.5
        reg_hour_pay = 40 * pay_rate
    else:
        overtime_hours = 0
        overtime_pay = 0
        reg_hour_pay = hours_worked * pay_rate
    
    # Calculate gross pay
    gross_pay = reg_hour_pay + overtime_pay
    
    # Update totals
    total_overtime += overtime_pay
    total_regular += reg_hour_pay
    total_gross += gross_pay
    employee_count += 1
    
    # Display individual employee results
    print("\nEmployee:", employee_name)
    print()
    print(f"Hours Worked   Pay Rate    OverTime    OverTime Pay     RegHour Pay     Gross Pay")
    print("-" * 90)
    print(f"{hours_worked:<14.1f}${pay_rate:<11.2f}{overtime_hours:<12.1f}${overtime_pay:<15.2f}${reg_hour_pay:<15.2f}${gross_pay:.2f}")
   

# Display final totals
print("\nTotal Number of Employees:", employee_count)
print("-" * 50)
print(f"Total amount paid for overtime: ${total_overtime:.2f}")
print(f"Total amount paid for regular hours: ${total_regular:.2f}")
print(f"Total amount paid in gross: ${total_gross:.2f}")
