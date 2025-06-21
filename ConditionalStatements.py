print("Welcome to Smart Login System")

username = input("Enter username: ")
password = input("Enter password: ")

# if condition
if username == "admin":
    print("Username is correct ")

    # if-else condition
    if password == "1234":
        print("Login successful")

        # using logical operators and nested if
        age = int(input("Enter your age: "))
        country = input("Enter your country: ")

        if age >= 18:
            if country.lower() == "india" or country.lower() == "usa":
                print("Access granted")
            else:
                print("Access denied: only allowed from India or USA")
        else:
            print("Access denied: You must be at least 18")

        # ternary conditional
        gender = input("Enter your gender (M/F): ")
        msg = "Welcome, Sir!" if gender.upper() == "M" else "Welcome, Ma'am!"
        print(msg)

        # if-elif-else
        marks = int(input("Enter your test marks out of 100: "))
        if marks >= 90:
            print("Grade: A+")
        elif marks >= 75:
            print("Grade: A")
        elif marks >= 60:
            print("Grade: B")
        elif marks >= 40:
            print("Grade: C")
        else:
            print("Grade: F (Fail)")

        # not operator and pass
        confirm = input("Do you want to log out? (yes/no): ")
        if not confirm.lower() == "yes":
            pass  # We'll add logout code later
            print("You stayed logged in")
        else:
            print("Logged out successfully")

    else:
        print("Wrong password")
else:
    print("Invalid username")
