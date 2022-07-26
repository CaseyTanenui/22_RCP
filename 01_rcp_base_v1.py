# Import Statements
import pandas

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

simple_borgir = yes_no("Would you like to learn how to make a Simple Burger?: ")    

if simple_borgir == "yes":
    print("Firstly, just go to burger king and purchase a burger")
    print("And then your done :)")
elif simple_borgir == "no":
    print("Okay")
    