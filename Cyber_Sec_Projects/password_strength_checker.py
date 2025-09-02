import re
import sys


print("Welcome to my password strength checker.")

def get_password():
    while True:
        
        pswd = str(input("Please enter what your password you would like to test is: "))
        if pswd == "":
            print("Please enter a password.")
            continue
            
        return pswd

def check_password(pswd):
    score = 0
    loweralpha = "abcdefghijklmnopqrstuvwxyz"
    upperalpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_check = "[!@#$%^&*()-_=+{}[];:,.<>?/|]"
    if len(pswd) < 8: #Checks that the password has a minimum input to be secure
        return score
    else:
        score += 1
    num_check = re.findall("[0-9]", pswd) # finds all the numbers in the passwords
    set_num = set(num_check)
    sorted_num = sorted(set_num)
    
    if len(num_check) >= 2: # checks if there is more than one number and that it is not the same number
        if len(num_check) == len(sorted_num):
            score += 1
    
    if any(char in special_check for char in pswd): # checks to see if the password contains a special char.
        score += 1
    
    if any(char in loweralpha for char in pswd) and any(char in upperalpha for char in pswd):
        score +=1   
    
    return score 
    
def password_strength(score):
    if score == 0:
        print("This password is very weak, please consider changing it. ")
    elif score == 1:
        print("This password is weak, please consider changing it. ")
    elif score == 2:
        print("This password is moderate. ")
    elif score == 3:
        print("This password is strong.")
    elif score == 4:
        print("This password is very strong.")
    
def another_test():
    while True:
        another = input("Would you like to try another password, Y or N").strip().lower()
        if another == 'y':
            break
        elif another == 'n':
            sys.exit()
        else:
            print("Please choose either Y or N: \n")
            continue
    
    



while True:
    pswd = get_password()
    score = check_password(pswd)
    password_strength(score)
    another_test()