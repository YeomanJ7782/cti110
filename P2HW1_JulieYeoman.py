 # Julie Yeoman

 # 10/9/2024

 # P2HW1

 # Edit and enhance existing programs
 
 
print("This program calculates and displays travel expenses")
print()

# Get user input
balance = float(input('Enter budget: '))
print()
destination = input("Enter your travel destination: ")
print()
gas_expense = float(input("How much do you think you will spend on gas? "))
print()
accommodation_expense = float(input("Approximately, how much will you need for accommodation/hotel? "))
print()
food_expense = float(input("Last, how much do you need for food? "))
print()

print("-----------Travel Expenses-----------")

# Calculate total expenses and remaining budget
total_expenses = gas_expense + accommodation_expense + food_expense
remaining_balance = balance - total_expenses

# Display results
print(f'Location: {destination:>23}')
print(f'Initial Budget: {"$" + f"{balance:.2f}":>12}')
print(f'Fuel: {"$" + f"{gas_expense:.2f}":>21}')
print(f'Accommodation: {"$" + f"{accommodation_expense:.2f}":>12}')
print(f'Food: {"$" + f"{food_expense:.2f}":>21}')
print('-------------------------------------')
print()
print(f'Remaining Balance: {"$" + f"{remaining_balance:.2f}":>8}')
