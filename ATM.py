import random  # For loading screen number
import csv  # For generating and reading usernames/passwords
import time  # For lockout feature


def start():
    print("Is this your first time using AIQ bank?")
    print("If it is please type 1 to create an account.")
    print("If not please type 2 to log in.")

    while True:
        try:
            user_choice = int(input("Enter your choice: "))

            if user_choice == 1:
                create()
            elif user_choice == 2:
                login()

            else:
                print("Please choose option 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number")
            print("testing CI/CD")


def create():
    print("Welcome to the AIQ bank account creation page")
    print("Please choose a username")

    while True:
        user_name = input("Enter a username: ")
        user_balance = 0

        if not user_name.isalpha():
            print("Invalid username. Only letters are allowed. Please try again.")
            continue

        try:
            user_password = int(input("Enter a 4-digit PIN: "))
            if len(str(user_password)) != 4:
                print("Invalid password, please try again.")
            else:
                with open("users.csv", mode="a", newline="") as file:
                    writer = csv.writer(file)
                    if file.tell() == 0:  # Create headers if the file is empty
                        writer.writerow(["Usernames", "Passwords", "Balance"])
                    writer.writerow([user_name, user_password, user_balance])

                print("AIQ Bank account created successfully.")
                start()

        except ValueError:
            print("Invalid input, please enter a 4-digit PIN.")
            continue


def login():
    print("Welcome to AIQ bank")

    max_attempts = 4
    attempts = 0

    while attempts < max_attempts:
        Username = input("Please enter your username: ")
        try:
            Userpin = int(input("Please enter your PIN: "))
        except ValueError:
            print("Invalid PIN format. Please enter a numeric PIN.")
            continue

        with open("users.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Usernames"] == Username and row["Passwords"] == str(Userpin):
                    print("Identity verified, login successful.")
                    print("Moving to menu, please wait")
                    time.sleep(2)

                    user_data = {
                        "Name": Username,
                        "Pass": Userpin,
                        "Bal": row.get("Balance"),
                    }
                    menu(user_data)
                    return  # Exit the login loop after successful login
            else:
                print("Incorrect username or PIN. Please try again.")
                attempts += 1

        if attempts < max_attempts:
            print(f"You have {max_attempts - attempts} attempts left.")
        else:
            print("Too many failed attempts. Please try again later.")
            print("AIQ bank will be locked for 60 seconds.")
            time.sleep(60)
            return


def menu(user_data):

    # mapping user choices to correct functions
    options = {
        1: pin,
        2: balance,
        3: signout,
        4: delete,
    }

    while True:
        print("welcome to the menu.")
        print("Your options are as following.")
        print("Type 1 to change your pin")
        print("Type 2 to check your balance")
        print("Type 3 to signout")
        print("Type 4 to delete your account")

        try:
            # getting user input
            choice = int(input("Enter your choice: "))
            if choice in options:
                # calling functions ring ring
                should_continue = options[choice](user_data)
                # exit loop if function is false aka dont exist
                if should_continue is False:
                    break
            else:
                print("Invalid choice. Please select a valid option")
        except ValueError:
            print("Invalid input. Please enter a number")

    print("Thank you for using the menu :)")


def pin(user_data):
    print("Welcome to the Pin change screen")
    print("For security reasons we require you to re-enter your PIN")
    user_pin = int(input("Enter your current PIN: "))
    while True:
        with open("users.csv", mode="r") as file:
            reader = csv.DictReader(file)

        for row in reader:
            if row["passwords"] == user_pin:
                print("PIN successfully verified, please")


def balance(user_data):
    print("Loading, please wait...")
    time.sleep(2)
    print(f"Hi {user_data['Name']}, your balance is {user_data['Bal']}.")
    print("Do you wish to sign out or go back to the main menu?")
    print("Type 1 for menu")
    print("Type 2 to sign out")

    while True:
        try:
            choice = int(input("Enter here: "))
            if choice == 1:
                menu(user_data)
            elif choice == 2:
                signout(user_data)
            else:
                print("Invalid input. Please enter either 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def delete(user_data):
    print("Placeholder")


def signout():
    print("Signing out, please wait")
    time.sleep(3)
    print("Signed out, thank you for using AIQ bank")
    start()


def add(user_data):
    print("placeholder")


def send(user_data):
    print("placeholder")


if __name__ == "__main__":
    random1 = random.randint(1, 20)
    random2 = random.randint(21, 40)
    random3 = random.randint(41, 60)
    random4 = random.randint(61, 80)
    random5 = random.randint(90, 100)

    print(f"Loading... {random1}%")
    print(f"Loading... {random2}%")
    print(f"Loading... {random3}%")
    print(f"Loading... {random4}%")
    print(f"Loading.. {random5}%")
    print("Loading complete,")
    print("AIQ Bank,")
    print("a service you can trust.")
    start()
