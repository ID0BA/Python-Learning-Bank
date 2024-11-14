import random  # For loading screen number
import csv  # For generating and reading usernames/passwords
import time  # For lockout feature


def start():
    print("Is this your first time using AIQ bank?")
    print("If it is please type 1 to create an account.")
    print("If not please type 2 to log in.")

    while True:
        try:
            user_input = int(input("Enter your choice: "))

            if user_input == 1:
                create()
                break
            elif user_input == 2:
                login()
                break
            else:
                print("Please choose option 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number")


def create():
    print("Welcome to the AIQ bank account creation page")
    print("Please choose a username")

    while True:
        user_name = input("Enter a username: ")  # username

        user_balance = 0  # creating value for user balance

        if (
            not user_name.isalpha()
        ):  # check if username is string only, took this outta the try loop since its not a valueError? right?
            print("Invalid username. Only letters are allowed. Please try again.")
            continue  # restart the loop

        try:
            user_password = int(
                input("Enter a 4 digit PIN: ")
            )  # convert password to interger

            if (
                len(str(user_password)) != 4
            ):  # check if password length is longer than 4 digits, god why doesnt len work with intergers took me way to long to solve this -_-
                print("Invalid password, please try again")
            else:

                with open(
                    "users.csv", mode="a", newline=""
                ) as file:  # creating file if it doesnt exist
                    writer = csv.writer(file)

                    if file.tell() == 0:  # creating table headers
                        writer.writerow(["Usernames", "Passwords, Balance"])

                    writer.writerow(
                        [user_name, user_password, user_balance]
                    )  # writing user data to file

                print("AIQ Bank account created successfully")
                start()
                break

        except ValueError:
            print("Invalid input, please enter a 4 digit PIN")
            continue  # restart the loop


def login():
    print("Welcome to AIQ bank")

    max_attempts = 4
    attempts = 0

    while attempts < max_attempts:
        Username = input("Please enter your username: ")
        Userpin = input("Please enter your PIN: ")

        with open("users.csv", mode="r") as file:
            reader = csv.DictReader(file)

            # looping thru rows to match data and user inputs
            for row in reader:
                if row["Usernames"] == Username and row["Passwords"] == Userpin:
                    print("Identity verified, login successful.")
                    print("Moving to menu, please wait")
                    time.sleep(2)
                    
                    # Store the user's information
                    user_data = {
                        "Name": Username,
                        "Pass": Userpin,
                        "Bal": row.get("Balance", "0")  # Retrieve balance, default to 0 if missing
                    }
                    # Pass user_data to the
                    menu(user_data)
                    break
            else:
                print("Incorrect username or PIN. Please try again.")
                attempts += 1

        if attempts < max_attempts:
            print(f"You have {max_attempts - attempts} attempts left.")
        else:
            print("Too many failed attempts. Please try again later.")
            print("AIQ bank will be locked for 60 seconds.")
            time.sleep(60)
            return False



def menu(user_data):
    print("welcome to the menu.")
    print("Your options are as following.")
    print("Type 1 to change your pin")
    print("Type 2 to check your balance")
    print("Type 3 to signout")
    print("Type 4 to delete your account")

    int(input("Enter your choice: "))

    if input == 1:
        pin(user_data)
    elif input == 2:
        balance(user_data)
    elif input == 3:
        signout(user_data)
    elif input == 4:
        delete(user_data)


def pin(user_data):
    print("Welcome to the Pin change screen")
    print("For security reasons we require you to re-enter your PIN")
    pin = int(input("Enter your current PIN: "))


def balance(user_data):
    
    print("Loading please wait")
    time.sleep(10)
    print(f"Hi {user_data['Name']}, your balance is {user_data["Bal"]} ")
    print("Do you wish to signout or go back to the main menu")
    print("Type 1 for menu")
    print("Type to signout")

    while True:
        choice1 = int(input("Enter here: "))
        if choice1 == 1:
            menu()
        elif choice1 == 2:
            signout()
        else:
            print("Invalid input please enter either 1 or 2")

def delete(user_data):
    print("Placeholder")


def signout(user_data):
    print("placeholder")
    exit()


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
