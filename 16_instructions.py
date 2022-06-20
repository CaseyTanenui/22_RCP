# Import Statements
import pandas 
import re

# -- Functions go here --

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

# Checks to see the users valid responses to the questions that are asked
# if not valid , shows error message
def string_check(choice, options):

    for var_list in options:

        # if the snack is in one of the lists, return the full item
        if choice in var_list:

            # Get full name of snack 

            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # If the options are not valid - set not_valid to no 
        else:
            is_valid = "no"

# Instructions on how to use this program
def instructions(options):
    show_help = "invalid choice"
    while show_help == "invalid choice":
        show_help = input("Would you like to read the instructions?: ")
        show_help = string_check(show_help, options)
    
    if show_help == "yes":
        print("-- Recipe Cost Calculator Information --")
        print("USE THIS PROGRAM IN THE INSTANCE")
        print("THAT YOU WOULD LIKE TO KNOW THE COST")
        print("OF THE RECIPE THAT YOU ARE COOKING/CONSUMING")
        print("To use this program, Enter the correct amount of")
        print("- Food items, The costs of each ingredient")
        print("- and the correct amount of servings you have chosen")
        print("Once you have correctly entered each one of the item")
        print("It will then calculate the correct amount of $ for each serving")
    return ""

# -- Main Routine starts here --