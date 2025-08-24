import sys


print("Welcome to my Calculator, What calculation would you like to perform: \n" +
      "Addition, Subtraction, Multiplication, or Division.\n" +
      "Type A(Addition), S(Subtraction), M(Multiplication), or D(Division)")
#This will indicate how the user wants to use the calculator
Selection = input("Calculation type: ").lower()

def get_numbers():
    '''
    
    This function retrieves the two numbers and checks that they are 
    valid numbers for a calculation.
    
    '''
    try: 
        print("Please enter the first number for the calculation: ")
        num1 = input()
        num1 = float(num1)
    except:
        print("This has to be a number, please try again.")
        get_numbers()
    try:   
        print("Please enter the second number for the calculation: ")
        num2 = input()
        num2 = float(num2)
    except: 
        print("This has to be a number, please try again.")
        get_numbers()
    return num1, num2
        
input1, input2 = get_numbers() # makes the numbers available for the the other functions.

def Addition():
    '''
    
    Adds the two numbers the user gave and prints the output.
    
    '''
    print("Addition it is!")
        #Adds the two numbers that the user gave together to give them the output.
    answer = input1 + input2   
    print(f"Answer: {answer:.2f}")
        
def Subtraction():
    '''
    
    Subtracts the two numbers the user gave and prints the output.
    
    '''
    print("Subtraction it is!")
    #Subtracts the two numbers given by the user to give an output.
    answer = input1 - input2
    print(f"Answer: {answer:.2f}")
    
def Multiplication():
    '''
    
    Multiplies the two numbers the user gave and prints the output.
    
    '''
    print("Multiplication it is!")
    #Multiplies the two numbers together that were given by the user,
    answer = input1 * input2
    print(f"Answer: {answer:.2f}")
    
def Division():
    '''
    
    Divides the two numbers the user gave and prints the output.
    
    '''
    print("Division it is!")
    try: 
        answer = input1 / input2
        print(f"Answer: {answer:.2f}")
    except:
        print("Cannot divide by zero!")
        sys.exit()

#This goes through the users selection and sees what arithmetic they want to use.    
if Selection.lower() == 'a':
    Addition()
elif Selection.lower() == 's': 
    Subtraction()
elif Selection.lower() == 'm':
    Multiplication()
elif Selection.lower() == 'd':
    Division()
else:
    print ("Please choose from the options listed.")
    
sys.exit()
    
    