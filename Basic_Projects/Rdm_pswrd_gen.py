import random  
import secrets
import sys

print("Welcome to the Random Password Generator!")

def getyesno(userinput):
    while True:
        option = input(userinput).strip().lower()
        if option in ("y", "n"):
            return option
        print("Please enter Y or N.")
        continue
            


def get_specifics():
    while True:
        try:
            length = int(input("How Long would you like this password (Required minimum 8)"))
            if length < 8:
                print("Please choose a length of at least 8.")
                continue
            
            lowercase = getyesno("Would you like to include lower case letters in your password, Y or N: ")
            uppercase = getyesno("Would you like to include upper case letters in your password, Y or N: ")
            numcase = getyesno("Would you like to include numbers in your password, Y or N: ")  
            specialcase = getyesno("Would you like to include special characters in your password, Y or N: ")
            
            if lowercase == 'n' and uppercase == 'n' and numcase == 'n' and specialcase == 'n':
                print("PLease choose at least one of the options given.")
                continue
            
            return length, lowercase, uppercase, numcase, specialcase
        except ValueError:
            print("Please choose a valid number for the length")
            continue

def random_gen(length, lowercase, uppercase, numcase, specialcase):
    loweralpha = "abcdefghijklmnopqrstuvwxyz"
    upperalpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    specialchar = "!@#$%^&*()-_=+{}[];:,.<>?/|"
    char_pool = ""
    password = []
    if lowercase == 'y':
        char_pool += loweralpha
        password.append(secrets.choice(loweralpha))
    if uppercase == 'y':
        char_pool += upperalpha
        password.append(secrets.choice(upperalpha))
    if numcase == 'y':
        char_pool += digits
        password.append(secrets.choice(digits))
    if specialcase == 'y':
        char_pool += specialchar
        password.append(secrets.choice(specialchar))
    for _ in range(length-len(password)):
        password.append(secrets.choice(char_pool))
    random.shuffle(password)
    passwordfinal = "".join(password)
    print("This is your generated password: " + passwordfinal + '\n')
    
def another_password():
    while True:
        leave = input("Do you want another password generated, Y or N").strip().lower()
        if leave == 'y':
            break
        if leave == 'n':
            sys.exit()
        else:
            print("Please choose either 'Y or 'N'.")
            continue
                      
while True:
    length, lowercase, uppercase, numcase, specialcase = get_specifics()
    random_gen(length, lowercase, uppercase, numcase, specialcase)
    another_password()
   