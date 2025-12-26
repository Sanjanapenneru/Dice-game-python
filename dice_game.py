import random

print("🎲 Welcome to Dice Game!")

# user rolls dice
input("Press Enter to roll the dice...")

user_roll = random.randint(1, 6)
computer_roll = random.randint(1, 6)

print("You rolled:", user_roll)
print("Computer rolled:", computer_roll)

# decide winner
if user_roll > computer_roll:
    print("🎉 You win!")
elif user_roll < computer_roll:
    print("😢 Computer wins!")
else:
    print("🤝 It's a tie!")
