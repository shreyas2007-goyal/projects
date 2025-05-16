def check_voting_eligibility():
    print("Welcome! Let's check if you are eligible to vote.")
    name = input("Enter your name: ")
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Age cannot be negative.")
        elif age >= 18:
            print(f"{name}, you are {age} years old. You are eligible to vote.")
        else:
            print(f"{name}, you are {age} years old. Not eligible to vote. Wait {18 - age} more years.")
    except ValueError:
        print("Please enter a valid number for age.")

check_voting_eligibility()