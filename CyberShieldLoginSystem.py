import msvcrt
import random 
import time

def password_input(message):

    password = ""

    print(message, end="", flush=True)

    while True:
        ch = msvcrt.getch().decode("utf-8")
        if ch == "\r":
            if len(password) < 4:
                print("\nPlease enter a 4 digit password")
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

password = password_input("Enter New Password: ")

while True:

    confirm_password = password_input("Confirm New Password: ")

    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        continue
    else:
        print("Password Successfully Saved")
        break



print("\nPlease enter the OTP showing below")
while True:
    otp = random.randint(1000, 9999)
    print("\nYour OTP:", otp)
    print("OTP is valid for 10 seconds")

    start_time = time.time()

    d = input("Enter the OTP: ")

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


while True:

    login= password_input("Enter Login Password: ")

    if password != login:
        print("Invalid password. Please try again.")
        continue
    else:
        print("Password Login Successfully")
        break

         
print("\033[94m \nwelcome to the python world 🌍\033")        
    