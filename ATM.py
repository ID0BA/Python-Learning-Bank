import random
import csv

def start():
    print("""Is this your first time using our bank? 
             If it is please type 1 to create your account. 
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
    print("Welcome to the bak account creation page")

    while True:
        user_name = input("Enter your name: ") # username

        if not user_name.isalpha():# check if username is string only, took this outta the try loop since its not a valueError? right? 
            print("Invalid username. Only letters are allowed. Please try again.")
            continue # restart the loop

        try:
            user_password = int(input("Enter a 4 digit PIN: ")) # convert password to interger

            if len(str(user_password)) !=4: # check if password length is longer than 4 digits, god why doesnt len work with intergers took me way to long to solve this -_-
                print("Invalid username or password, please try again")
            else:
                
                with open("users.csv", mode="a", newline="") as file: # creating file if it doesnt exist
                    writer = csv.writer(file)

                    if file.tell() == 0: # creating table headers
                        writer.writerow({"Usernames", "Passwords"})

                    writer.writerow([user_name, user_password]) # writing user data to file
                
                print("Account created successfully")
                start()
                break

        except ValueError:
            print("Invalid input, please eneter a valid 4 digit PIN")
            continue # restart the loop

def login():
    print("placeholder")

if __name__ == "__main__":
    random1 = random.randint(1, 20)
    random2 = random.randint(21, 40)
    random3 = random.randint(41, 60)
    random4 = random.randint(61, 80)
    random5 = random.randint(81, 100)
    
    print(f"Loading... {random1}%")
    print(f"Loading... {random2}%")
    print(f"Loading... {random3}%")
    print(f"Loading... {random4}%")
    print(f"Loading.. {random5}%")
    print("""Loading complete,
            Welcome.""")
    start()