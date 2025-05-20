import random

while True:
    # User input
    print("\nChoose between Barbie, Chewing Gum, or Gun (type 'stop' to exit)")
    your_choice = input("Enter your choice: ").strip().lower()

    # Exit condition
    if your_choice == "stop":
        print("Thanks for playing! Goodbye 👋")
        break  # Exit the loop

    # Dictionary for conversion
    yourdic = {'barbie': 0, 'chewing gum': 1, 'gun': 2}
    revdic = {0: 'Barbie', 1: 'Chewing Gum', 2: 'Gun'}

    # Handling invalid input
    if your_choice not in yourdic:
        print("Invalid choice! Please enter 'Barbie', 'Chewing Gum', or 'Gun'.")
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