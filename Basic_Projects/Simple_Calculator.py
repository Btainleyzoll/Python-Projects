import sys


print("Welcome to my Calculator, where you can make simple arithmetic calculations!")
prev = 0 #initiating the variable for later use
first_time = True  
ans_list = []
equation_list = [] 
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
    
    def additional_calc():
            '''
            
            Gives the user the option to make another calculation or exit the
            system.
            
            '''
            while True:
                print("\nChoose from one of the following:\n" + 
                    "Type '1' to make another simple calculation.\n" +
                    #"Type '2' to make your own equation(Not working as of now)\n" +
                    "Type '3' to show a list of the previous answers\n" +
                    "Type '4' to exit the calculator.")
                rerun = input()
                if rerun == '1':
                    break
                #elif rerun == '2':
                #   complex_equation()
                elif rerun == '3':
                    view_prev_answers()
                elif rerun == '4':
                    print("Goodbye!")
                    sys.exit()
                else:
                    print("Please choose from one of the options listed.")
                    continue
                    
    def get_numbers():
        '''
        
        This function retrieves the two numbers and checks that they are 
        valid numbers for a calculation.
        
        '''
        while True:
            try: 
                print("Please enter the first number for the calculation: ")
                num1 = str(input().lower().strip())
                if num1.lower() == "prev":
                    num1 = prev
                num1 = float(num1)
                break
            except ValueError:
                print("This has to be a number, please try again.")
                
        while True:        
            try:   
                print("Please enter the second number for the calculation: ")
                num2 = str(input().lower().strip())
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
            #Adds the two numbers that the user gave together to give them the output.
        ans = input1 + input2   
        print(f"\nAnswer: {ans:.2f}")
        return ans    
    def Subtraction():
        '''
        
        Subtracts the two numbers the user gave and prints the output.
        
        '''
        #Subtracts the two numbers given by the user to give an output.
        ans = input1 - input2
        print(f"\nAnswer: {ans:.2f}")
        return ans
        
    def Multiplication():
        '''
        
        Multiplies the two numbers the user gave and prints the output.
        
        '''
        #Multiplies the two numbers together that were given by the user,
        ans = input1 * input2
        print(f"\nAnswer: {ans:.2f}")
        return ans
        
    def Division():
        '''
        
        Divides the two numbers the user gave and prints the output.
        
        '''
        try: 
            ans = input1 / input2
            print(f"\nAnswer: {ans:.2f}")
            return ans
        except ZeroDivisionError:
            print("Cannot divide by zero!")
            additional_calc()
            
    '''def complex_equation():
        
        
        This function will allow the user to type in a equation that will be solved 
        and it can be more complex than just a 2 number arithmetic. It will return the
        answer after going through the whole equation. 
        
        
        print("Welcome to the complex calculator.\n" +
              "Below, write out your equation that you want solved. " +
              "Example: 12+7-5/2*4=, and when your finished it will print the output.")
        equation = str(input().lower())
        number = ""
        output = []
        stack = []
        for y in equation:
            
            if y.lower().isdigit() or y.lower() == '.' or y.lower() == [-1]:
                number += y
                continue
            else:
                if number:
                    equation_list.append(number)
                    number = ""
                if y.strip():
                    equation_list.append(y)
                
        if number:
              equation_list.append(number)  
        print(equation_list)
        
        for d in equation_list:
            if d.isdigit():
                output.append(d)'''
            
            
        
        
        
        
    def view_prev_answers():
        '''
        
        This function returns a list of all the previous answers that were calculated.
        
        '''
        while True:
            print("These are your previous calculations made on the calculator: ")
            for number, i in enumerate(ans_list, start = 1):
                print(number, i)
            print("When you are done, type '1' to go back to the menu.")
            goback = input()
            if goback == '1':
                additional_calc()
                break
            else:
                print("Please press '1' when you are finished looking at the previous answers.")
        
        
        

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
    prev = round(prev, 2)
    ans_list.append(prev)
    additional_calc()
    

    
    