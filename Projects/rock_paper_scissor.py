import random
choices = ["r", "p", "s"]
emojis = {"r": "Rock 🪨", "p": "Paper 📄", "s": "Scissors ✂️"}
user_choice = input("Enter your choice (r for rock, p for paper, s for scissors): ").lower()
if user_choice not in choices:
    print("Invalid input. Please enter r, p, or s.")

computer_choice = random.choice(choices)
print(f"Computer chose: {emojis[computer_choice]}")
print(f"User chose: {emojis[user_choice]}")
if user_choice == computer_choice:
    print("It's a tie!")
    
elif (user_choice == "r" and computer_choice == "s") or \
     (user_choice == "p" and computer_choice == "r") or \
     (user_choice == "s" and computer_choice == "p"):
    print("You win!")
else:
    print("Computer wins!")
