import random

print("Dice Simulator")

results = []
user = input("Do you want to roll dice (yes/no): ").lower().replace(" ", "")
if user == "yes":
    try:
        no_dice = int(input("How many times do you want to roll the dice: "))
        if no_dice <= 0:
            print("Please enter a positive number.")
        else:
            for _ in range(no_dice):
                dice = random.randint(1, 6)
                results.append(dice)
            print(f"You rolled: {results}")
    except ValueError:
        print("Invalid number. Please enter a valid integer.")
elif user == "no":
    print("You selected no!")
else:
    print("Invalid input...")
