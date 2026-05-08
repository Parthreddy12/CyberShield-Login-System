import msvcrt
import random 
import time

def password_input(message):

    password = ""

    print(message, end="", flush=True)

    while True:
        ch = msvcrt.getch().decode("utf-8")
        if ch == "\r":
            # password = input("Enter password: ")

            if len(password) < 8:
                print("Password must contain 8 characters")
                password = ""
                print(message, end="", flush=True)
                continue

            elif not any(ch.isupper() for ch in password):
                print("Password must contain uppercase letter")
                password = ""
                print(message, end="", flush=True)
                continue

            elif not any(ch.islower() for ch in password):
                print("Password must contain lowercase letter")
                password = ""
                print(message, end="", flush=True)
                continue

            elif not any(ch.isdigit() for ch in password):
                print("Password must contain number")
                password = ""
                print(message, end="", flush=True)
                continue

            elif not any(ch in "~!@#$%^&*()_+}{|:<>?[];',./" for ch in password):
                print("Password must contain special character")
                password = ""
                print(message, end="", flush=True)
                continue

            else:
                print("\nPassword Accepted")
                return password

        elif ch == "\b":
            if len(password) > 0:
                password = password[:-1]
                print("\b \b", end="", flush=True)

        else:
            password += ch
            print("*", end="", flush=True)


print("\033[94m \nWelcome to Cyber Shield Login System 🔐")
print("\nPlease create a new password for your account.")
print("""
Minimum 8 characters
At least 1 uppercase letter
At least 1 lowercase letter
At least 1 number
At least 1 special character
\033[0m""")
password = password_input("\nEnter New Password: ")

while True:

    confirm_password = password_input("\nConfirm New Password: ")

    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        continue
    else:
        print("Password Successfully Saved")
        break


try:
    print("\nPlease enter the OTP showing below")
    while True:
        otp = random.randint(1000, 9999)
        print("\nYour OTP:", otp)
        print("OTP is valid for 10 seconds")

        start_time = time.time()

        d = input("\nEnter the OTP: ")

        end_time = time.time()

        if end_time - start_time > 10:
            print("Time expired! Generating new OTP...")
            continue

        if d == "":
            print("Please enter the OTP")
            continue

        if int(d) != otp:
            print("Please enter valid OTP")
            continue

        print("OTP matched")
        break
except Exception as e:
    print("You have entered invalid input. Please try again.")  

while True:

    login= password_input("\nEnter Login Password: ")

    if password != login:
        print("Invalid password. Please try again.")
        continue
    else:
        print("Password Login Successfully")
        break

         
print("\033[94m \nwelcome to the python world 🌍\033[0m")        
    