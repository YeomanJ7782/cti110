# Julie Yeoman
# 10/26/2024
# P3HW2
# This program calculates employee's gross salary including overtime with 1.5 rate

'''
Pseudocode / Algorithm:
1. Display program title
2. Get input from user:
   - Employee name
   - Number of hours worked
   - Pay rate per hour
3. Calculate payments:
   - Check if hours > 40 for overtime
   - If overtime:
     * Calculate overtime hours (hours - 40)
     * Calculate overtime pay (overtime hours * pay rate * 1.5)
     * Calculate regular pay (40 * pay rate)
   - If no overtime:
     * Calculate regular pay (hours * pay rate)
   - Calculate gross pay (regular pay + overtime pay)
4. Display results:
   - Employee name
   - Pay rate
   - Hours worked
   - Overtime hours
   - Overtime pay
   - Regular hour pay
   - Gross pay
'''

# Get input from user
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Calculate overtime hours and pay
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

# Display results
print("-" * 50)
print("Employee name:", employee_name)
print()
print(f"Hours Worked   Pay Rate    OverTime    OverTime Pay     RegHour Pay     Gross Pay")
print("-" * 90)
print(f"{hours_worked:<14.1f}${pay_rate:<11.2f}{overtime_hours:<12.1f}${overtime_pay:<15.2f}${reg_hour_pay:<15.2f}${gross_pay:.2f}")
