import sys


print("Welcome to my Calculator, What calculation would you like to perform: \n" +
      "Addition, Subtraction, Multiplication, or Division.\n" +
      "Type A(Addition), S(Subtraction), M(Multiplication), or D(Division)")
#This will indicate how the user wants to use the calculator
Selection = input("Calculation type: ").lower()
num1 = float(input("First number: "))
        
num2 = float(input("Second number: "))

def Addition():
    '''
    Returns the sum of num1 and num2.
    
    Parameters:
        num1(float): first number
        num2(float): second number
    
    '''
    print("Addition it is!")
        #Adds the two numbers that the user gave together to give them the output.
    answer = num1 + num2   
    print(answer)
        
def Subtraction():
    print("Subtraction it is!")
    #Subtracts the two numbers given by the user to give an output.
    answer = num1 - num2
    print(answer)
    
def Multiplication():
    print("Multiplication it is!")
    #Multiplies the two numbers together that were given by the user,
    answer = num1 * num2
    print(answer)
    
def Division():
    print("Division it is!")
    try: 
        answer = num1 / num2
        print(answer)
    except:
        print("Cannot divide by zero!")
        sys.exit()
    
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
    
    