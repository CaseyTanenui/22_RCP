# Import Statements
import pandas
import math

# Checks that user has entered either 'yes' or 'no'...
# If user has said 'no' code breaks
# If user has said 'yes' code continues
# Error message shows when an unexpected 
# Value has been entered...
def yes_no(question):

    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return var_item
            elif response == var_item[0]:
                return var_item
                
        print("Please enter either yes or no...\n")

# Number checking function...
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))
            
            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# Checks that user has not completed anything with blank errors
def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)
    
        if response == "":
            print("{}. \nPlease try again.\n".format(error))
            continue

        return response

# Gets recipe name, recipe information
# And all serving sizes
def get_recipe(var_fixed, question, error):

    # Dictionarys to hold the recipe
    recipe_name = []
    recipe_information = []
    recipe_servings = []

