"""LU base component - based on 00_LU_base_v1
Components added after they have been created and tested
Added 06_rounds_v3
Changed the format on line 118 to currency
"""

import random


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


# Number checking function
def num_check(question, low, high):
    error = "That was not a valid input\n" \
            "Please enter a number between {} and {}\n".format(low, high)

    # Keep asking until a valid amount (1, 10) is entered
    while True:
        try:
            # Ask for amount
            response = int(input(question))

            # Check for number within required range
            if low <= response <= high:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# Function to generate token
def generate_token(balance):
    rounds_played = 0
    play_again = ""

    # Testing loop to generate 5 tokens
    while play_again != "x":
        rounds_played += 1  # keep track of rounds
        number = random.randint(1, 100)  # can only be a donkey

        # Adjust balance
        # If random number is between 1 and 5
        # User gets a unicorn (add $4 to balance)
        if 1 <= number <= 5:
            token = "unicorn"
            balance += 4
            print(formatter("!", "Congratulations, you got an unicorn"))
            print()

        # If the random number is between 6 and 36
        # User gets a donkey (subtract $1 to balance)
        elif 6 <= number <= 36:
            token = "donkey"
            balance -= 1

        # In all other cases the token must be a horse or a zebra
        # (subtract $0.50 to balance in either case)
        else:
            # If number is even, set the token to zebra
            if number % 2 == 0:
                token = "zebra"
                balance -= 0.50

                # Otherwise, set the token to horse
            else:
                token = "horse"
                balance -= 0.50

    # Output
    print(f"Round {rounds_played}. Token: {token}, Balance: ${balance}")
    if balance < 1:
        print(f"\nSorry but you have run out of money")
        play_again = "x"
    else:
        play_again = input("\nDo you want to play another round?\n<enter>to play "
                           "again or 'X' to exit").lower()
        print()
        return balance


# Function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main Routine goes here...
print(formatter("-", "Welcome to the Lucky Unicorn Game"))
print()
played_before = yes_no("Have you played this game before?")

if played_before == "No":
    instructions()

# ask the user how much they want to play with
starting_balance = num_check("How much would you like to play with? $", 1, 10)
print(f"You are now playing with ${starting_balance}")

closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"You started with ${starting_balance:.2f}"
      f"and left with ${closing_balance:.2f}")
print()
print(formatter("*", "Goodbye"))
