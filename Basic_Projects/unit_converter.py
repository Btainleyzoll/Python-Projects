print("Welcome to my unit converter! \n" +
      "This will be able to convert most units from one to another easily.")



    
def convert_to_weight(converter, heavy):
    '''
    This will find what the user wants to convert the weight to.        
    '''
    while True:
        print("Choose the number that corresponds to what weight you want to convert to:\n" +
                "1. Grams\n" +
                "2. Kilograms\n" +
                "3. Ounces\n"
                "4. Pounds\n" +
                "5. Stones")
        valid_options = {"1": "Grams", 
                        "2": "Kilograms",
                        "3": "Ounces",
                        "4": "Pounds",
                        "5": "Stones"}
        input2 = input().strip().lower()
        if converter == input2:
            print("You can't convert to the same unit.")
            continue
        elif input2 in valid_options:
            print(f"You are converting {heavy} {valid_options[converter]} to {valid_options[input2]}.")
            conversion_factors = {
                "Grams": {
                    "Kilograms": 1/1000,
                    "Ounces": 1/28.35,
                    "Pounds": 1/453.592,
                    "Stones": 1/6350.29
                },
                "Kilograms": {
                    "Grams": 1000,
                    "Ounces": 35.274,
                    "Pounds": 2.20462,
                    "Stones": 0.157473
                },
                "Ounces": {
                    "Grams": 28.35,
                    "Kilograms": 1/35.274,
                    "Pounds": 1/16,
                    "Stones": 1/224
                },
                "Pounds": {
                    "Grams": 453.592,
                    "Kilograms": 1/2.20462,
                    "Ounces": 16,
                    "Stones": 1/14
                },
                "Stones": {
                    "Grams": 6350.29,
                    "Kilograms": 6.35029,
                    "Ounces": 224,
                    "Pounds": 14
                }
            }
            converted = heavy * conversion_factors[valid_options[converter]][valid_options[input2]]
            converted = round(converted, 2)
            print(f"The converted weight is {converted} {valid_options[input2]}.")
            break  
            
def amount(converter):
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
        convert_to_weight(converter, heaviness)
        return heaviness
    
def weight():
    '''
    Asks the user which weight unit they want to convert from.
        
        
     '''
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
            heaviness = amount(input1)
            return input1, heaviness
                
        else:
            print("Please choose from the options listed")
            continue
        
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
            converter, heavy = weight()
            break
        elif type == '3':
            #dosomething
            break
        else:
            print("Please choose from the options given.")

while True:
    type_of_unit()


        
    
        
            
            
                
            
                        
                            
                    
        
    
         
    
          