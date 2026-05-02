import random
def no_guessing():
    no_to_guess = random.randint(1, 100)
    while True:
        try:
            choice1 = int(input("Enter a number between 1 and 100: "))
            if no_to_guess < choice1:
                print("High! Try again.")
            elif no_to_guess > choice1:
                print("Low! Try again.")
            elif no_to_guess == choice1:
                print(f"Congratulations! You guessed the number {no_to_guess }.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            print("Invalid input. Please enter a number between 1 and 100.")
no_guessing() 