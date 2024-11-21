# Julie Yeoman
# November 16 2024
# P5LAB - Self-Checkout Change Dispenser
# This program simulates a self-checkout machine that calculates the change owed to a customer
# and displays how many dollars, quarters, dimes, nickels, and pennies are needed.

import random

# Function to calculate and disperse the change
def disperse_change(change):
    # Calculate the number of dollars, quarters, dimes, nickels, and pennies
    dollars = int(change // 1)
    change -= dollars
    quarters = int(change // 0.25)
    change -= quarters * 0.25
    dimes = int(change // 0.10)
    change -= dimes * 0.10
    nickels = int(change // 0.05)
    change -= nickels * 0.05
    pennies = round(change / 0.01)  # Round to the nearest penny to avoid floating point errors

    # Display the change breakdown
    print()
    if dollars > 0:
        print(f"{dollars} Dollars")
    if quarters > 0:
        print(f"{quarters} Quarters")
    if dimes > 0:
        print(f"{dimes} Dimes")
    if nickels > 0:
        print(f"{nickels} Nickels")
    if pennies > 0:
        print(f"{pennies} Pennies")

# Main function to simulate the self-checkout
def main():
    # Generate a random amount for the total owed by the customer
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${total_owed}")

    # Prompt the user for the amount they will pay
    amount_paid = float(input("How much cash will you put in the self-checkout?: $"))

    # Calculate the change to be returned
    if amount_paid < total_owed:
        print("Insufficient funds! Please enter an amount greater than the total owed.")
    else:
        change_owed = round(amount_paid - total_owed, 2)
        print(f"Change is: ${change_owed}")
        
        # Call the disperse_change function to calculate and display the change
        disperse_change(change_owed)

# Call the main function to run the program
if __name__ == "__main__":
    main()
