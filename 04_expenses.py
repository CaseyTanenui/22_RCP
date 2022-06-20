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

rcp_name = not_blank("What is the name of the recipe?: ", "The name cannot be blank")
print()
rcp_price = num_check("What is the exact price of each ingredient?:  ", "sorry - it has to be more than 0", float)
print()
rcp_servings = num_check("What serving sizes are we working with?: ", "sorry - it cannot be less than 0", int)
print()

serving_price = rcp_price / rcp_servings

print("-- Recipe Name: {} --".format(rcp_name))
print("Price per Serving: ${:.2f}".format(serving_price))