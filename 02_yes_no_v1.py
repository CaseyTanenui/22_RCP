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

# Loops to make testing faster...
for item in range(0,6):
    want_help = yes_no("Do you want to read the instructions? ")
    print("You said '{}'\n".format(want_help))