# Import Statements..
import re
import pandas
import math

# -- Functions goes Here --

# Checks that input is either a float or 
# an interger that is more than zero, Takes in custom error message
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

# Checks that user has entered either 'yes' or 'no'...
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

# Checks that user has not completed anything with blank errors
def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)
    
        if response == "":
            print("{}. \nPlease try again.\n".format(error))
            continue

        return response

# Rounding function...
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to

# -- Main Routine goes Here --

# Lists to hold ingredients, serving sizes and ingredient prices..


# Checks to see the recipe name 
# Checks to see the Ingredient prices
# Checks to see the Serving sizes
# and gets all of them..
def get_expenses(var_fixed):

    # Setup dictionaries
    rcp_name = []
    rcp_ingredients = []
    rcp_price = []
    rcp_servings = []

    # Loop ingredients and prices
    rcp_loop = 0

    # Variable Dictionary for items, prices and servings
    variable_dict = {
        "Name": rcp_name,
        "Ingredients": rcp_ingredients,
        "Price": rcp_price,
        "Servings": rcp_servings,
        "Total": serving_price
    }

    # Loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":

        rcp_name = not_blank("What is the name of the recipe?: ", "The name cannot be blank".format(rcp_loop +1))
        print()
        rcp_ingredient = not_blank("What are the ingredients?: ", "This component cannot be blank".format(rcp_loop +1))
        print()
        rcp_price = num_check("What is the exact price of each ingredient?:  ", "sorry - it has to be more than 0".format(rcp_loop +1), float)
        print()
        rcp_servings = num_check("What serving sizes are we working with?: ", "sorry - it cannot be less than 0".format(rcp_loop +1), int)
        print()

        # Add item, quantity and price to lists
        rcp_name.append(rcp_name)
        rcp_ingredients.append(rcp_ingredients)
        rcp_price.append(rcp_price)
        rcp_servings.append(rcp_servings)
        serving_price.append(serving_price)
    
        # Calculate how much it would cost per serving..
        serving_price = rcp_price / rcp_servings

        return [serving_price]