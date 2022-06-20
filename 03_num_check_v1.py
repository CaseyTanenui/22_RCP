# Import Statements
import re
import pandas

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

# Looping to make the testing faster
for item in range(0,6):
    num_elif = num_check("How much?: ")
    print("you gave me '{}'\n".format(num_elif))

