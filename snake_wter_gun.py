import random

while True:
    # User input
    print("\nChoose between snake, water, or gun (type 'stop' to exit)")
    your_choice = input("Enter your choice: ").strip().lower()

    # Exit condition
    if your_choice == "stop":
        print("Thanks for playing! Goodbye 👋")
        break  # Exit the loop

    # Dictionary for conversion
    yourdic = {'snake': 0, 'water': 1, 'gun': 2}
    revdic = {0: 'snake', 1: 'water', 2: 'gun'}

    # Handling invalid input
    if your_choice not in yourdic:
        print("Invalid choice! Please enter 'snake', 'water', or 'gun'.")
        continue  # Restart the loop

    # Random choice for computer
    computer = random.choice([0, 1, 2])
    you = yourdic[your_choice]

    print(f'You chose {revdic[you]}\nComputer chose {revdic[computer]}')

    # Game logic
    if computer == you:
        print("It's a draw!")
    elif (you == 0 and computer == 2) or (you == 1 and computer == 0) or (you == 2 and computer == 1):
        print("You lose! 😢")
    else:
        print("You win! 🎉")