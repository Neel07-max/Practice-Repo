import random

number = random.randint(1, 100)
print("Welcome to the Guessing Game!")

while True:
    try:
        guess = int(input("Enter your guess: "))

        if guess == number:
            print("🎉 Congratulations! You guessed the number correctly.")
            break
        elif guess > number:
            print("⬆ Too high! Try again.")
        else:
            print("⬇ Too low! Try again.")

    except ValueError:
        print("❌ Please enter a valid integer.")
print(f"The correct number was: {number}")