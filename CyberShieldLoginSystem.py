import msvcrt
import random 

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
otp= random.randint(1000,9999)
print(otp)
d = int(input("Enter the OTP: "))
if d!=otp:
    print("please enter valid OTP")
while d!=otp:
    otp= random.randint(1000,9999)
    print(otp)
    d  = int(input("Enter the OTP: "))
    if d!=otp:    
        print("please enter valid OTP")
    else:
        print("OTP matched ") 


while True:

    login= password_input("Enter Login Password: ")

    if password != login:
        print("Invalid password. Please try again.")
        continue
    else:
        print("Password Login Successfully")
        break

         
print("\033[94m \nwelcome to the python world 🌍\033")        
    