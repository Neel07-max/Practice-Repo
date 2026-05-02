import random
def guess_number():
    choice = input("Press Y/y to roll the dice...").lower()
    if choice == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"Die 1: {die1}, Die 2: {die2}")
    elif choice == "n":
        print("Exiting the game. Goodbye!")
    else:      
        print("Invalid input. Please enter Y/y to roll the dice or N/n to exit.")
        guess_number()
guess_number()