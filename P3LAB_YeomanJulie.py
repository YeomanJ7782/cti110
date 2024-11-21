#Name: Julie Yeoman
#Date: October 20th, 2024
#Assignment: P3LAB
#Description: This program calculates the most efficient number of dollars and coins needed to make up a given amount of money.


def calculate_change(amount):
    # Check if amount is zero
    if amount == 0:
        return ["No change"]

    # Convert the amount to cents
    cents = int(amount * 100)
    
    # Initialize variables for each denomination
    dollars = cents // 100
    cents %= 100
    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    pennies = cents % 5
    
    # Create a list of tuples with the count and name of each denomination
    denominations = [
        (dollars, "dollar", "dollars"),
        (quarters, "quarter", "quarters"),
        (dimes, "dime", "dimes"),
        (nickels, "nickel", "nickels"),
        (pennies, "penny", "pennies")
    ]
    
    # Generate the output list
    output = []
    for count, singular, plural in denominations:
        if count > 0:
            name = singular if count == 1 else plural
            output.append(f"{count} {name}")
    
    return output

# Main program
try:
    amount = float(input("Enter the amount of money as a float: $"))
    if amount < 0:
        print("Please enter a non-negative amount.")
    else:
        result = calculate_change(amount)
        print(f"${amount:.2f} is:")
        for item in result:
            print(item)
except ValueError:
    print("Invalid input. Please enter a valid number.")
