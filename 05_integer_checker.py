# Number Checker
# There is a very useful Python 'cheat sheet' in the support files area
# We can create a piece of code to ensure that users enter a valid number
# by combining a while loop and try / except code”

# Ask user for number
# Loop question so that it repeats until valid number is entered
# Make code recyclable!

# function goes here
def intcheck(question, low, high):
    valid = False
    while not valid:
        error = "Whoops! Please enter an integer between {} " \
                "and {}".format(low, high)

        try:
            response = int(input("Enter an integer between {} "
                                 "and {}: ".format(low, high)))

            if low <= response <= high:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)

# main routine goes here

num_1 = intcheck("Enter a number between 1 and 15", 1, 15)
num_2 = intcheck("Enter a number between 5 and 10", 5, 10)