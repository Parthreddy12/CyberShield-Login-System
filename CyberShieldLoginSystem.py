import getpass as gp

a = (gp.getpass("Enter the new password: ")) 
if a<1000:
    print("Please enter 4 digit number password")
while a<1000:
    a = (gp.getpass("Enter the new password: "))
    if a<1000:
       print("Please enter 4 digit number password")
    else:
        pass
        
b = int(input("Confirm the new password: "))
if a!=b:
    print("invalid password")
else:
    pass
while a!=b:
    a = (gp.getpass("Enter the new password: "))
    b = (gp.getpass("Confirm the new password: "))
    if a!=b:
        print("invalid password")
    else:
        print("continue ")    

c = (gp.getpass("Enter the password: "))
if c!=a:
        print("invalid password \nplease enter correct password")

while c!=a:
    c = (gp.getpass("Enter the password: "))
    if c!=a:
        print("invalid password \nplease enter correct password")
    else:
        print("correct password")    
        
import random 
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
      
       
print("\033[94mwelcome to the python world 🌍")        
    