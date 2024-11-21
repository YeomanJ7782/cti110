# Julie Yeoman
# 9/29/2024
# P1HW2
# This program computes basic math on numbers that are entered

#1. Display program title
#2. Get user's budget as input
#3. Get travel destination as input
#4. Get gas expense as input
#5. Get accommodation expense as input
#6. Get food expense as input
#7. Calculate total expenses of gas, accommodation, and food
#8. Calculate remaining budget (budget minus total expenses)
#9. Display travel destination
#10. Display initial budget
#11. Display all expenses
#12. Display total expenses
#13. Display remaining budget



# Program Code
print("This program calculates and displays travel expenses")
print()

# Get user input
balance = float(input('Enter budget: '))
print()
destination = input("Enter your travel destination: ")
print()
gas_expense = float(input("How much do you think you will spend on gas? "))
print()
accommodation_expense = float(input("Approximately, how much will you need for accomidation/hotel? "))
print()
food_expense = float(input("Last, how much do you need for food? "))
print()
print("--------Travel Expenses--------")

# Calculate total expenses and remaining budget
total_expenses = gas_expense + accommodation_expense + food_expense
remaining_balance = balance - total_expenses

# Display results
print(f'Location: {destination:>13}')
print(f'Initial Budget: ${balance:>10.2f}')
print(f'Fuel: ${gas_expense:.2f}')
print(f'Accommodation: ${accommodation_expense:.2f}')
print(f'Food: ${food_expense:.2f}')
print('-------------------------------')
print(f'Remaining Balance: ${remaining_balance:.2f}')

