# Program performs and records simple calculations

print("=============================================")
print(" Welcome to ABC Simple Calculator")
print(" Ready when you are!")
print("=============================================")

operations = {1:"Addtion",
              2:"Subtraction",
              3:"Multiplication",
              4:"Division"
              }

records = []

# Calculations stored in fuction *Note to self function can take as many arguments*
def calculations(x_int, y_int, user_selection):
    """
    Calculate the result and equation of a user's calculation

    Parameters:
    x_int (int): First integer
    y_int (int): Second integer
    user_selection (int): Determines which operation is executed (+, -, *, ÷)
    
    Returns:
    result (int/float): The result/answer of x_int & y_int
    equation (string): stored in 'records' (which is a list), used to write into equations.txt file
    """

    
    if user_selection == 1:
        result = x_int + y_int
        equation = f"{x_int} + {y_int} = {x_int + y_int}"
        return result, equation
    elif user_selection == 2:
        result = x_int - y_int
        equation = f"{x_int} - {y_int} = {x_int - y_int}"
        return result, equation
    elif user_selection == 3:
        result = x_int * y_int
        equation = f"{x_int} * {y_int} = {x_int * y_int}"
        return result, equation
    elif user_selection == 4:
        if y_int == 0:
            return None, "Error by zero division, chief"
        result = x_int / y_int
        equation = f"{x_int} / {y_int} = {x_int / y_int}"
        return result, equation
    else:
         return None, "Invalid operation"



while True:
    try:
        # Displaying options for user
        print("\nSelect an operation")
        for key, value in operations.items():
             print(f"{key}. {value}")

        # Prompt user for intgers
        x_int = int(input("Please enter your first integer: "))
        y_int = int(input("Please enter your second integer: "))
        
        # Prompt user for input
        user_selection = int(input("Please select a operation from the menu above: "))

        # Printing result and adding the equation to 'records' list 
        result, equation = calculations(x_int, y_int, user_selection)
        if result is not None:
            print(f"Result:{result}")
            records.append(str(equation))
        else:
             print(equation)
        
        # Creating equations text file and writing each equation into the file 
        with open("equations.txt","a") as file:
                    file.write( equation + "\n")
        

        # Prompt user, if they want more calculation
        while True:
            user_option = input("Do you want to calculate more equations ? (y/n): ").lower()
            if user_option == "y":
                break
            elif user_option =="n":
                print("Thanks for participating.")
                exit()
            else:
                print("Opps! Try again. 'y' or 'n'")   
            
    # User enters a string as opposed to an integer 
    except ValueError:
        print("Not a valid entry. Integers only.")


