import sys


print("Welcome to my Calculator, where you can make simple arithmetic calculations!")
prev = 0 #initiating the variable for later use
first_time = True     
while True:
    #Runs this if statement only during the first start to this loop so printing text will be different the rest of the loops.
    if first_time:
        print("What calculation would you like to perform: \n" +
        "Addition, Subtraction, Multiplication, or Division.\n" +
        "Type A(Addition), S(Subtraction), M(Multiplication), or D(Division)")
        #This will indicate how the user wants to use the calculator
        Selection = input("Calculation type: ").lower()
        
    if not first_time:
        print("What type of calculation would you like to make " +
              "Addition(A), Subtraction(S), Multiplication(M), or Division(D)?\n" +
              "Also if you would like to use your previous answer, when putting " + 
              "a number in, put 'prev'.")
        Selection = input("Calculation type: ").lower()
    first_time = False

    def get_numbers():
        '''
        
        This function retrieves the two numbers and checks that they are 
        valid numbers for a calculation.
        
        '''
        while True:
            try: 
                print("Please enter the first number for the calculation: ")
                num1 = str(input())
                if num1.lower() == "prev":
                    num1 = prev
                num1 = float(num1)
                break
            except ValueError:
                print("This has to be a number, please try again.")
                
        while True:        
            try:   
                print("Please enter the second number for the calculation: ")
                num2 = str(input())
                if num2.lower() == "prev":
                    num2 = prev
                num2 = float(num2)
                break
            except ValueError: 
                print("This has to be a number, please try again.")
                
        return num1, num2
            
    input1, input2 = get_numbers() # makes the numbers available for the the other functions.

    def Addition():
        '''
        
        Adds the two numbers the user gave and prints the output.
        
        '''
        print("Addition it is!")
            #Adds the two numbers that the user gave together to give them the output.
        ans = input1 + input2   
        print(f"Answer: {ans:.2f}")
        return ans    
    def Subtraction():
        '''
        
        Subtracts the two numbers the user gave and prints the output.
        
        '''
        print("Subtraction it is!")
        #Subtracts the two numbers given by the user to give an output.
        ans = input1 - input2
        print(f"Answer: {ans:.2f}")
        return ans
        
    def Multiplication():
        '''
        
        Multiplies the two numbers the user gave and prints the output.
        
        '''
        print("Multiplication it is!")
        #Multiplies the two numbers together that were given by the user,
        ans = input1 * input2
        print(f"Answer: {ans:.2f}")
        return ans
        
    def Division():
        '''
        
        Divides the two numbers the user gave and prints the output.
        
        '''
        print("Division it is!")
        try: 
            ans = input1 / input2
            print(f"Answer: {ans:.2f}")
            return ans
        except:
            print("Cannot divide by zero!")
            sys.exit()
            
    def additional_calc():
        '''
        
        Gives the user the option to make another calculation or exit the
        system.
        
        '''
        print("\nWould you like to make another calculation, Y or N?")
        rerun = input().lower()
        if rerun.lower() == 'y':
            print("Will do!")
        elif rerun.lower() == 'n':
            sys.exit()
        else:
            print("Please choose either Y or N to make another calculation.")
            additional_calc()
        

    #This goes through the users selection and sees what arithmetic they want to use.    
    if Selection.lower() == 'a':
        prev = Addition()
    elif Selection.lower() == 's': 
        prev = Subtraction()
    elif Selection.lower() == 'm':
        prev = Multiplication()
    elif Selection.lower() == 'd':
        prev = Division()
    else:
        print ("Please choose from the options listed.")
    additional_calc()
    

    
    