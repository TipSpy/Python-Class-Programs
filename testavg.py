#Test Score Averages
#This program uses nested loops

# This program averages test scores. It asks the user for the
# number of students and the number of test scores per student.

# Get the number of students
num_students = int(input('How many students do you have? '))

# Get the number of test scores per student.
num_test_scores = int(input('How many test scores per student? '))

# Determine each students average test score.
for student in range(num_students):
    # initialize an accumulator for test scores.
    total = 0.0
    # Get a students test scores.
    print('Student number', student + 1)
    print('-------------------')
    for test_num in range(num_test_scores):
        print('Test Number', test_num + 1)
        score = float(input(': '))
        # Add the score to the accumulator
        total += score

        # calculate the average test score for this student
        average = total / num_test_scores

        # Display the average
        print('The average for student number', student + 1, \
              'is:', format(average, '.2f'))
        print()