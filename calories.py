#Calories

# Global constants for calories
CALORIES_FROM_FAT = 9
CALORIES_FROM_CARBS = 4

# main module
def main():
    #Local Variables
    gramsFat = 0.0
    gramsCarbs = 0.0
    caloriesFat = 0.0
    caloriesCarbs = 0.0

    # Get grams fat.
    gramsFat = float(input('Enter the fat grams consumed: '))

    # Get grams carbs.
    gramsCarbs = float(input('Enter the carbohydrate grams consumed: '))

    # Calculate calories from fat
    caloriesFat = gramsFat * CALORIES_FROM_FAT

    # Calculate calories from carbs
    caloriesCarbs = gramsCarbs * CALORIES_FROM_CARBS

    #Print the calories.
    showCarbs(gramsFat, gramsCarbs, caloriesFat, caloriesCarbs)

#The showCarbs function accepts the number of grams of fat and
# of carbs, as well as the calories from fat and from carbs, as
# arguments and displays the resulting calories.
def showCarbs(gramsFat, gramsCarbs, caloriesFat, caloriesCarbs):
    print('Grams of fat: ', format(gramsFat, '.2f'))
    print('Fat Calories: ', format(caloriesFat, '.2f'))
    print('Grams of carbs: ', format(gramsCarbs, '.2f'))
    print('Carb Calories: ', format(caloriesCarbs, '.2f'))

# Call the main function
main()