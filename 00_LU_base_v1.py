"""LU base component
Components added after they have been created and tested"""


# Yes/No checking function
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes,output 'Program Continues'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output 'Display Instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Please answer Yes or No")

# Function to display instructions
def instructions():
    print("**** How to Play ****")
    print()
    print("The rules of the game will go here")
    print()
    print("Program continues")
    print()


# Main Routine goes here...
played_before = yes_no("Have you played this game before?")

if played_before == "No":
    instructions()
else:
    print("Program Continues")
