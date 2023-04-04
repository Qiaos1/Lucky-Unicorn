"""Component 4 - game mechanics and looping v2
Based on 06_rounds_v1
removed hard-wiring so that all token can be allocated (randint 1-100)
Gives user feedback about the number of rounds and maintains balance
Test amount set to $5
"""

import random

# Main routine
TEST_AMOUNT = 5
balance = TEST_AMOUNT

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

print("Thanks for playing")
print(f"You started with ${TEST_AMOUNT:.2f}"
      f"and left with ${balance:.2f}")
print("Goodbye")
