 #Julie Yeoman

 #10/11/2024

 #P2HW2

 #Create a list to show understanding of concept

#BEGIN Program

#Create a list to store grades
 #DECLARE grades AS LIST

#Prompt user for each module grade
#PRINT "Enter the grade for Module 1:"
#INPUT grade1
#APPEND grade1 TO grades

#PRINT "Enter the grade for Module 2:"
#INPUT grade2
#APPEND grade2 TO grades

#PRINT "Enter the grade for Module 3:"
#INPUT grade3
#APPEND grade3 TO grades

#PRINT "Enter the grade for Module 4:"
#INPUT grade4
#APPEND grade4 TO grades

#PRINT "Enter the grade for Module 5:"
#INPUT grade5
#APPEND grade5 TO grades

#PRINT "Enter the grade for Module 6:"
#INPUT grade6
#APPEND grade6 TO grades

# Calculate the required outputs
#SET lowest_grade AS MINIMUM OF grades
#SET highest_grade AS MAXIMUM OF grades
#SET sum_of_grades AS SUM OF grades
#SET average_grade AS sum_of_grades DIVIDED BY LENGTH OF grades

# Display the results
#PRINT "Lowest grade: ", lowest_grade
#PRINT "Highest grade: ", highest_grade
#PRINT "Sum of grades: ", sum_of_grades
#PRINT "Average grade: ", FORMAT(average_grade, ".2f")

#END Program





# Create a list to store grades
grades = []

# Prompt user for each module grade
grades.append(float(input("Enter the grade for Module 1: ")))
grades.append(float(input("Enter the grade for Module 2: ")))
grades.append(float(input("Enter the grade for Module 3: ")))
grades.append(float(input("Enter the grade for Module 4: ")))
grades.append(float(input("Enter the grade for Module 5: ")))
grades.append(float(input("Enter the grade for Module 6: ")))

# Calculate the required outputs
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

# Display the results
print('------------Results----------')
print("Lowest grade: ", lowest_grade)
print("Highest grade: ", highest_grade)
print("Sum of grades: ", sum_of_grades)
print("Average grade: {:.2f}".format(average_grade))
print('----------------------------------------')
