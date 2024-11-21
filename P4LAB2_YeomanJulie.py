# Yeoman Julie
# November 2 2024
# P4LAB2
# Creating a program that asks user for integer and displays multiplication table

def display_multiplication_table(n):
    """Display the multiplication table from 1 to 12 for a given integer n."""
    for i in range(1, 13):  # Loop from 1 to 12
        print(f"{n} x {i} = {n * i}")

def main():
    while True:  # While loop to ask the user if they want to run again
        try:
            num = int(input("Enter an integer: "))  # Get user input and convert to integer
        except ValueError:
            print("Please enter a valid integer.")
            continue  # If input is not a valid integer, ask again

        if num >= 0:  # If the number is zero or higher
            display_multiplication_table(num)  # Display the multiplication table
        else:
            print("This program does not handle negative numbers.")  # If number is negative

        # Ask the user if they want to run again using a while loop
        repeat = input("Do you want to run again? (yes/no): ").lower().strip()
        while repeat not in ['yes', 'no']:  # Input validation for "yes" or "no"
            repeat = input("Please answer with 'yes' or 'no': ").lower().strip()
        
        if repeat == 'no':
            print("Exiting program...")
            break  # Exit the while loop and end the program

# Call the main function to start the program
main()
