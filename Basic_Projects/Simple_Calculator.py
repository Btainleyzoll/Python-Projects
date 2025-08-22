print("Welcome to my Calculator, What calculation would you like to perform: \n" +
      "Addition, Subtraction, Multiplication, or Division.\n" +
      "Type A(Addition), S(Subtraction), M(Multiplication), or D(Division)")
#This will indicate how the user wants to use the calculator
Selection = input("Calculation type: ").lower()

def Addition():
    '''
    Returns the sum of num1 and num2.
    
    Parameters:
        num1(float): first number
        num2(float): second number
    
    '''
    print("Addition it is!\n")
    num1 = float(input("First number: "))
        
    num2 = float(input("Second number: "))
        #Adds the two numbers that the user gave together to give them the output.
    answer = num1 + num2
        
    print(answer)
        
def Subtraction():
    '''
    Returns the difference of num1 and num2.
    
    Parameters:
        num1(float): first number
        num2(float): second number
    
    '''
    print("Subtraction it is!\n")
    num1 = float(input("First Number: "))
    
    num2 = float(input("Second number: "))
        #Subtracts the two numbers given by the user to give an output.
    answer = num1 - num2
    print(answer)
    
    
    
    
if Selection.lower() == 'a':
    Addition()
elif Selection.lower() == 's': 
    Subtraction()
else:
    print ("Please choose from the options listed.")
    
    