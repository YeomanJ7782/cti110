# Julie Yeoman
# November 10, 2024
# P4HW1
# This program collects scores from user input, validates them, calculates the average after dropping the lowest score, and assigns a letter grade.

"""
Pseudocode:
1. Welcome user and get number of scores to enter
2. Create empty list for scores
3. For each score:
    a. Get score from user
    b. While score is invalid (not between 0-100):
        - Display error
        - Ask for valid score
    c. Add valid score to list
4. Find and store lowest score
5. Remove lowest score from list
6. Calculate average of remaining scores
7. Determine letter grade based on average
8. Display results:
    - Lowest score
    - Modified list
    - Average
    - Letter grade
"""

def get_valid_score():
    """Get a valid score between 0 and 100 from the user."""
    while True:
        try:
            score = float(input("Enter score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("\nINVALID Score entered!!!!")
                print("Score should be between 0 and 100")
        except ValueError:
            print("\nINVALID Score entered!!!!")
            print("Score should be a number between 0 and 100")

def get_letter_grade(average):
    """Convert numerical average to letter grade."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

# Main program
# Get number of scores
while True:
    try:
        num_scores = int(input("\nHow many scores do you want to enter? "))
        if num_scores > 0:
            break
        print("Please enter a positive number.")
    except ValueError:
        print("Please enter a valid number.")

# Collect scores
scores = []
for i in range(num_scores):
    score = get_valid_score()
    scores.append(score)

# Calculate results
lowest_score = min(scores)
modified_scores = scores.copy()
modified_scores.remove(lowest_score)
average = sum(modified_scores) / len(modified_scores)
letter_grade = get_letter_grade(average)

# Display results
print("\n--------------Results--------------")
print("Lowest Score  :", lowest_score)
print("Modified List :", modified_scores)
print(f"Scores Average: {average:.2f}")
print(f"Grade        : {letter_grade}")
print("----------------------------------")
