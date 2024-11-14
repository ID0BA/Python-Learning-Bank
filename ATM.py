import random
import csv
import time

def start():
    print("""Is this your first time using AIQ bank? 
             If it is please type 1 to create an account. 
             If not please type 2 to log in.
          """)
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

    while True:
        user_name = input(""""Enter a username
                          Please note only letters are allowed
                        : """) # username

        if not user_name.isalpha():# check if username is string only, took this outta the try loop since its not a valueError? right? 
            print("Invalid username. Only letters are allowed. Please try again.")
            continue # restart the loop

        try:
            user_password = int(input("Enter a 4 digit PIN: ")) # convert password to interger

            if len(str(user_password)) !=4: # check if password length is longer than 4 digits, god why doesnt len work with intergers took me way to long to solve this -_-
                print("Invalid password, please try again")
            else:
                
                with open("users.csv", mode="a", newline="") as file: # creating file if it doesnt exist
                    writer = csv.writer(file)

                    if file.tell() == 0: # creating table headers
                        writer.writerow({"Usernames", "Passwords"})

                    writer.writerow([user_name, user_password]) # writing user data to file
                
                print("AIQ Bank account created successfully")
                start()
                break

        except ValueError:
            print("Invalid input, please enter a 4 digit PIN")
            continue # restart the loop

def login():
    print("Welcome to AIQ bank")

    # setting max number of attempts allowed to prevent exploitation
    max_attempts = 4 
    attempts = 0

    #checks how many attempts have been made
    while attempts < max_attempts:
        
        Username=input("Please enter your username: ") #gathering username and pin
        Userpin=input("Please enter your PIN: ")

        #opening csv and comparing stored creds against user inputs
        with open ("users.csv", mode="r") as file:
            reader=csv.DictReader(file)

            for row in reader:
                if row["Usernames"] == Username:
                    if row['Passwords'] == Userpin:
                        print("Identity verified, login successful.")
                        print("Moving to menu, please wait")
                        time.sleep(5)
                        menu()
                    else:
                        print
                        print("incorrect Pin please try again")
                        attempts += 1
                        break
                else:
                    print("incorrect username please try again")
                    attempts += 1
                    break
        if attempts < max_attempts:
            print(f"you have {max_attempts - attempts} attempts left")
        else:
            print("Too many failed attempts. Please try again later.")
            print("AIQ bank will be locked for 60 seconds")
            time.sleep(60)
            return False

def menu():
    int(input("""welcome to the menu.
          Please select what you wish to do.
          Type 1 to change your pin
          Type 2 to check your balance
          Type 3 to delete your account
          Type 4 to signout"""))
    if input == 1:
        pin()

def pin():
    print("""
          Welcome to the Pin change screen
          For security reasons we require you to re-enter your PIN""")
    
    pin = int(input("Enter your current PIN: "))


def balance():
    print("Placeholder")

def delete():
    print("Placeholder")

def signout():
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
    print("""Loading complete,
            AIQ Bank, 
          a service you can trust.""")
    start()