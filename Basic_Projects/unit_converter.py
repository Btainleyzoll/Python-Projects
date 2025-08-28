print("Welcome to my unit converter! \n" +
      "This will be able to convert most units from one to another easily.")


while True:
    
    def weight():
        while True:
            print("Choose the number that corresponds to what weight you want to convert from:\n" +
                    "1. Grams\n" +
                    "2. Kilograms\n" +
                    "3. Ounces\n"
                    "4. Pounds\n" +
                    "5. Stones")
             #Makes a list of the valid options the user can choose from to check against the user input.
            valid_options = {"1": "Grams", 
                             "2": "Kilograms",
                             "3": "Ounces",
                             "4": "Pounds",
                             "5": "Stones"}
            input1 = input().strip().lower()
            if input1 in valid_options:
                amount()
                return input1
                    
            else:
                print("Please choose from the options listed")
                continue
    
                    
                
    def amount():
        '''
        Gets the user to input the starting amount for the converter to use. 
        This function is only used for length and weight.
        
        '''
        while True:
            print("What is the initial amount?")
            heaviness = input().strip()
            try:
                heaviness = float(heaviness)
            except:
                print("Please print a valid number.")
                continue
            if heaviness < 0:
                print("This number mustn't be negative.")
                continue
            convert_to_weight()
            break
            
            
    def convert_to_weight():
        '''
        This will find what the user wants to convert the weight to.
        
        '''
    
    
    def type_of_unit():
        '''
        
        This function will find out which unit type the user wants to convert
        and will then give the appropriate output depending on their answer.
        
        '''
        while True:
            print("Choose which type of units would you like to convert: \n" +
                "1. Length\n" +
                "2. Weight\n" +
                "3. Temperature")
            type = input().strip()
            if type == '1':
                #dosomething
                break
            elif type == '2':
                weight()
                break
            elif type == '3':
                #dosomething
                break
            else:
                print("Please choose from the options given.")
                
    type_of_unit()
    converter = weight()           
    def Length():
        print("Length")
        
    
        
            
            
                
            
                        
                            
                    
        
    
         
    
          