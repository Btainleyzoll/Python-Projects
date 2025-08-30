print("Welcome to my unit converter! \n" +
      "This will be able to convert most units from one to another easily.")



def convert_to_length(converter1, length):
    '''
    This will find what the user wants to convert the length to.        
    '''
    while True:
        print("Choose the number that corresponds to what length you want to convert to:\n" +
                "1. Meters\n" +
                "2. Kilometers\n" +
                "3. Centimeters\n" +
                "4. Feet" +
                "5. Miles\n" +
                "6. Yards\n" +
                "7. Inches")
        valid_options = {"1": "Meters", 
                        "2": "Kilometers",
                        "3": "Centimeters",
                        "4": "Feet",
                        "5": "Miles",
                        "6": "Yards",
                        "7": "Inches"}
        input2 = input().strip().lower()
        if converter1 == input2:
            print("You can't convert to the same unit.")
            continue
        elif input2 in valid_options:
            print(f"You are converting {length} {valid_options[converter1]} to {valid_options[input2]}.")
            conversion_factors = {
                "Meters": {
                    "Kilometers": 1/1000,
                    "Centimeters": 100,
                    "Feet": 3.28084,
                    "Miles": 1/1609.34,
                    "Yards": 1.09361,
                    "Inches": 39.3701
                },
                "Kilometers": {
                    "Meters": 1000,
                    "Centimeters": 100000,
                    "Feet": 3280.84,
                    "Miles": 0.621371,
                    "Yards": 1093.61,
                    "Inches": 39370.1
                },
                "Centimeters": {
                    "Meters": 1/100,
                    "Kilometers": 1/100000,
                    "Feet": 0.0328084,
                    "Miles": 1/160934,
                    "Yards": 0.0109361,
                    "Inches": 0.393701
                },
                "Feet": {
                    "Meters": 0.3048,
                    "Kilometers": 0.0003048,
                    "Centimeters": 30.48,
                    "Miles": 1/5280,
                    "Yards": 1/3,
                    "Inches": 12}
            }
            converted1 = length * conversion_factors[valid_options[converter1]][valid_options[input2]]
            converted1 = round(converted1, 2)
            print(f"The converted length is {converted1} {valid_options[input2]}.")
            break
          
def convert_to_weight(converter2, heavy):
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
        if converter2 == input2:
            print("You can't convert to the same unit.")
            continue
        elif input2 in valid_options:
            print(f"You are converting {heavy} {valid_options[converter2]} to {valid_options[input2]}.")
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
            converted2 = heavy * conversion_factors[valid_options[converter2]][valid_options[input2]]
            converted2 = round(converted2, 2)
            print(f"The converted weight is {converted2} {valid_options[input2]}.")
            break  
def length_amount(converter1):
    '''
    Gets the user to input the starting amount for the converter to use. 
    This function is only used for length and weight.
     
    '''
    while True:
        print("What is the initial Length?")
        lengthiness = input().strip()
        try:
            lengthiness = float(lengthiness)
        except:
            print("Please print a valid number.")
            continue
        if lengthiness < 0:
            print("This number mustn't be negative.")
            continue
        convert_to_length(converter1, lengthiness)
        return lengthiness
    
def amount(converter2):
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
        convert_to_weight(converter2, heaviness)
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
        
def Length():
    while True:
        
        print("Choose the number that corresponds to what length you want to convert from:\n" +
                "1. Meters\n" +
                "2. Kilometers\n" +
                "3. Centimeters\n" +
                "4. Feet\n" +
                "5. Miles\n" +
                "6. Yards\n" +
                "7. Inches")
        input1 = input().strip().lower()
         #Makes a list of the valid options the user can choose from to check against the user  
        valid_options = {"1": "Meters", 
                        "2": "Kilometers",
                        "3": "Centimeters",
                        "4": "Feet",
                        "5": "Miles",
                        "6": "Yards",
                        "7": "Inches"}
        if input1 in valid_options:
            Lengthiness = length_amount(input1)
            return input1, Lengthiness
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
            converter1, lengthiness = Length()
            break
        elif type == '2':
            converter2, heavy = weight()
            break
        elif type == '3':
            #dosomething
            break
        else:
            print("Please choose from the options given.")

while True:
    type_of_unit()


        
    
        
            
            
                
            
                        
                            
                    
        
    
         
    
          