# making a calculator 
print("Enter the value infort like 6 + 7 (space is necessary)\n(for now this is only made for 2 digit calculations)")#information
def calculator(a, b, c): # function for calculation
    if b == "+": # for adding
        plue = a+c
        return plue  
    elif b == "*": # for multipliying
        multiply = a*c
        return multiply
    elif b == "/": # for dividing
        divide = a/c
        return divide
    elif b == "-": # for subtratcing
        subtract = a-c
        return subtract
    else: # in case if user enterd PURE str VALUE
        print("ERROR")            
def ask(): # function to get the value and making it  
    while True:
        eu = input("value = ") # asking the value from user
        if eu.lower() == "break":# breaking the loop
            print("goodbye") # greetings
            break       
        x, y, z = eu.split()
        x, y, z = float(x), y, float(z) # making it flot not int
        print(calculator(x, y, z))#after converting it to the float using the calculator function      
#loop is implemented on the ask function 
ask()
