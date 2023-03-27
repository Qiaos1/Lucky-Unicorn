"""LU Yes / No
Puts the code created in v2 into a loop to make testing easier and more
efficient.
"""

show_instructions = ""
while show_instructions != "x":
    # Ask the user if they have played before
    show_instructions = input("Have you played this game before?: ").lower()

    # If they say yes,output 'Program Continues'
    if show_instructions == "yes" or show_instructions == "y":
        print("Program continues")

    # If they say no, output 'Display Instructions'
    elif show_instructions == "no" or show_instructions == "n":
        print("Display instructions")

    # Otherwise - show error
    else:
        print("Please answer Yes or No")

    print(f"You entered '{show_instructions}'")

