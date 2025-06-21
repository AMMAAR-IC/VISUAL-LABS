print("Welcome to the Smart Loop Tool\n")

while True:
    print("\nChoose an option:")
    print("1. Print Even Numbers (for loop + continue)")
    print("2. Password Checker (while loop + break)")
    print("3. Print Star Triangle (nested loop)")
    print("4. Number Guessing Game (while + else)")
    print("5. Exit")

    choice = input("Enter your choice (1–5): ")

    # for loop with continue
    if choice == "1":
        print("Even numbers from 1 to 20:")
        for i in range(1, 21):
            if i % 2 != 0:
                continue  # skip odd numbers
            print(i, end=' ')
        print()

    # while loop with break
    elif choice == "2":
        tries = 3
        while tries > 0:
            pwd = input("Enter password (hint: 'open123'): ")
            if pwd == "open123":
                print("Access granted")
                break
            else:
                print("Wrong password")
                tries -= 1
        else:
            print("Too many attempts. Account locked")

    # nested loop for pattern printing
    elif choice == "3":
        rows = int(input("Enter number of rows: "))
        print("★ Star Triangle ★")
        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end='')
            print()

    # while with else (guessing game)
    elif choice == "4":
        import random
        secret = random.randint(1, 10)
        guess = None
        attempts = 3

        while attempts > 0:
            guess = int(input("Guess a number between 1–10: "))
            if guess == secret:
                print("Correct! You win.")
                break
            else:
                print("Wrong guess.")
                attempts -= 1
        else:
            print(f"Game over! The number was {secret}.")

    elif choice == "5":
        print("Exiting. Thanks for using the Smart Loop Tool.")
        break

    else:
        print("Invalid choice. Try again.")
