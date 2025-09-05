'''
This is my password Strength checker where you can input a password,
and the functions will run various checks to see how secure this 
password actually is and will output a prompt letting the user know
if there password is strong or should be augmented.
'''
import re
import sys
from collections import Counter


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
    elif len(pswd) >= 8:
        score += 1
        if len(pswd) >= 12:
            score += 1
        if len(pswd) >= 16:
            score += 2
    num_check = re.findall("[0-9]", pswd) # finds all the numbers in the passwords
    set_num = set(num_check)
    sorted_num = sorted(set_num)
    
    if len(num_check) >= 2: # checks if there is more than one number and that it is not the same number
        if len(num_check) == len(sorted_num):
            score += 1
    
    if re.search(special_check, pswd): # checks to see if the password contains a special char.
        score += 1
    
    if any(char in loweralpha for char in pswd) and any(char in upperalpha for char in pswd):
        lower_check = re.findall("[a-z]", pswd)
        upper_check = re.findall("[A-Z]", pswd)
        set_lower = set(lower_check)
        set_upper = set(upper_check)
        sorted_lower = sorted(set_lower)
        sorted_upper = sorted(set_upper)
        if len(sorted_lower) == len(lower_check) and len(sorted_upper) == len(upper_check):
            score +=3
        else:
            total = len(pswd)
            lower_counts = Counter(lower_check)
            upper_counts = Counter(upper_check)
            if max(lower_counts.values(), default=0) / total > 0.3:
                score -=3
            
            if max(upper_counts.values(), default=0) / total > 0.3:
                score -=3
                    
        score +=1 
          
    if score >= 4:
        score += 3
        
    return score 
    
def password_strength(score):
    if score >=0 and score <= 2:
        print("This password is very weak, try using more characters and special characters. ")
    elif score >=3 and score <= 5:
        print("This password is moderately weak, please consider changing it. ")
    elif score >= 6 and score <= 8:
        print("This password is moderately strong. ")
    elif score <= 8:
        print("This password is very strong, good job. ")
    elif score <0:
        print("This password is incredibly weak, please add more characters and special characters and numbers. ")
    
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