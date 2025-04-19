import random  # For loading screen number
import csv  # For generating and reading usernames/passwords
import time  # For lockout feature
import os
import uuid


class Bankuser:
    def __init__(self, username="", password="", balance=0.0):
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.password = password
        self.balance = balance
        self.is_locked = False

    def create_account(self):
        # Prompt user for account details
        self.username = input("Enter your username: ").strip()
        self.password = input("Enter your password: ").strip()
        self.balance = float(random.randint(0, 100))

        # Save account details to CSV
        self.save_to_csv()

        time.sleep(0.5)
        print(f"Account for {self.username} was created successfully!")
        print(f"Your starting balance is £{self.balance}")
        print("Navigating to menu")
        self.menu()

    def save_to_csv(self):
        file_path = "Details.csv"

        try:
            # Check if the file exists and is not empty
            file_exists = os.path.exists(file_path) and os.path.getsize(file_path) > 0

            # Open the file in append mode
            with open(file_path, mode="a", newline="") as file:
                writer = csv.writer(file)

                # Write headers if the file is empty
                if not file_exists:
                    writer.writerow(["User_ID", "Username", "Password", "Balance"])

                # Write the account details
                writer.writerow(
                    [self.user_id, self.username, self.password, f"{self.balance:.2f}"]
                )
        except Exception as e:
            print(f"An error occurred while saving to CSV: {e}")

    def menu(self):
        print("Placeholder")

    def login(self):
        print("placeholder")

    def change_details(self):
        print("placeholder")

    def delete_account(self):
        ("placeholder")

    def add_money(self):
        ("placeholder")

    def withdraw_money(self):
        print("placeholder")

    def transfer_money(self):
        print("placeholder")

    def account_lock(self):
        if self.is_locked:
            print("Account is locked. Please contact customer service.")
            return True
        return False


def loading_screen():
    loading_steps = [
        random.randint(1, 20),
        random.randint(21, 40),
        random.randint(41, 60),
        random.randint(61, 80),
        random.randint(90, 100),
    ]

    for i in loading_steps:
        print(f"Loading... {i}%")
        time.sleep(0.5)

    print("Loading complete.")
    print("AIQ Bank a service you can trust.")


if __name__ == "__main__":
    loading_screen()
    user = Bankuser()
    user.create_account()
