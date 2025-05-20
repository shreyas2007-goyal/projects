import random

while True:
    # User input
    print("\nChoose between stone, paper, or scissors (type 'stop' to exit)")
    your_choice = input("Enter your choice: ").strip().lower()

    # Exit condition
    if your_choice == "stop":
        print("Thanks for playing! Goodbye 👋")
        break  # Exit the loop

    # Dictionary for conversion
    yourdic = {'stone': 0, 'paper': 1, 'scissors': 2}
    revdic = {0: 'stone', 1: 'paper', 2: 'scissors'}

    # Handling invalid input
    if your_choice not in yourdic:
        print("Invalid choice! Please enter 'stone', 'paper', or 'scissors'.")
        continue  # Restart the loop

    # Random choice for computer
    computer = random.choice([0, 1, 2])
    you = yourdic[your_choice]

    print(f'You chose {revdic[you]}\nComputer chose {revdic[computer]}')

    # Game logic
    if computer == you:
        print("It's a draw! 😐")
    elif (you == 0 and computer == 2) or (you == 1 and computer == 0) or (you == 2 and computer == 1):
        print("You win! 🎉")
    else:
        print("You lose! 😢")
