
#========The beginning of the class==========
class Shoe:
    """ 
    Represents a Nike shoe stock inventory

    Attributes:
    country (str): Location of warehouse
    code (str): ID number for each shoe type
    product (str): Name of shoe
    cost (int): Cost of a single pair
    quantity (int): Number of units per pair of shoe

    """

    def __init__(self, country, code, product, cost, quantity):
        '''
        
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''

        # Defining instance variables of Shoe class
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        '''
        Determines the cost of a single pair of shoes.

        Returns:
            integer: (self.cost = cost)
        
        '''

        return self.cost


    def get_quantity(self):
        '''
        Determines the number of pair of shoes (units).

        Returns:
            integer: (self.quantity = quantity)
        
        '''

        return self.quantity
    

    def __str__(self):
        '''
        Determines the string representation of Shoe class.

        Returns:
            country (str): Location of warehouse
            code (str): ID number for each shoe type
            product (str): Name of shoe
            cost (int): Cost of a single pair
            quantity (int): Number of units per pair of shoe

        '''

        return ("-----Shoe Details-----\n"
                f"Country: {self.country}\n"
                f"Code: {self.code}\n"
                f"Product: {self.product}\n"
                f"Cost: R{self.cost}\n"
                f"Quantity: {self.quantity}\n")



#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


#==========Functions outside the class==============
def read_shoes_data():
    '''
    Opens and reads inventory text file with each line representing
    as a single shoe object of the Shoe class.

    Returns:
        list = shoe_list, a list containing each line of the text file as a single object,
                 thus a list of shoe objects of the Shoe class

    '''

# Adding all inventory data in text file to shoe_list.
    try:
        with open("inventory.txt","r") as file:
            for index,line in enumerate(file):
                 if index == 0:
                     continue
                 else:
                     country, code, product, cost, quantity = line.strip().split(",")
                     shoe_list.append(Shoe(country,code,product,int(cost),int(quantity)))                   
    
    # Error handling if file does not exist
    except FileNotFoundError: 
        print("The file does not exist. Please check the file path and try again")
    
    return shoe_list
          

def capture_shoes(shoe_list):
    '''
    Enable user to create a new shoe object via entering 
    the relevant information defining a shoe object.

    Proompt user for country,code,product,cost and quantity
    New objects are then added to existing shoe_list

    '''

    while True:
        try:
            no_of_shoes = int(input("Enter the number of shoes to add to database: "))
            if no_of_shoes > 0:
                break
            else:
                print("Oops.. The number you wish to add is negative")
        except ValueError:
            print("Invalid entry. Please try again")

    for i in range(no_of_shoes):      
        print(f"\n-----Enter detail for Shoe No. {i+1} of {no_of_shoes}-----")
        
        # Captures Country
        while True:
            input_Country = input("Please enter the Country: ").strip()
            if input_Country:
                break
            else:
                print("Country attribute cannot be empty")
        
        # Captures Code
        while True:
            input_Code = input("Please enter the Code: ").strip()
            if input_Code.isalnum(): # alphanumeric validates entry is both strings and integers
                break
            else:
                print("Code may be invalid. Please try again")

        # Captures Product
        while True:
            input_Product = input("Please enter the Product: ").strip()
            if input_Product:
                break
            else:
                print("Product name cannot be empty")
            
        # Captures Cost   
        while True:
            try:
                input_Cost = int(input("Please enter the Cost: "))
                if input_Cost > 0:
                    break
                else:
                    print("The cost of a shoe cannot be negative")
            except ValueError:
                print("Digits only... Please try again")
        
        # Captures Quantity
        while True:
            try:
                input_Quantity = int(input("Please enter the Quantity: "))
                if input_Quantity >= 0:
                    break
                else:
                    print("The quantity of shoes cannot be negative")
            except ValueError:
                print("Digits only... Please try again")

        new_shoe = Shoe(country=input_Country,code=input_Code,product=input_Product,cost=input_Cost,quantity=input_Quantity)
        shoe_list.append(new_shoe)

        # Save new_shoe(s) to text file
        with open("inventory.txt","a") as file:
            file.write(f"{new_shoe.country},{new_shoe.code},{new_shoe.product},{new_shoe.cost},{new_shoe.quantity}\n")
    return shoe_list


def view_all(shoe_list):
    '''
    Dispalys details of objects(shoes) in shoe_list, uses _str_ method in Shoe class
    
    '''
    
    print("\n-----Shoes in Database-----")
    for index,shoe in enumerate(shoe_list,start=1):
        print(f"Shoe: {index}\n{shoe}")


def re_stock(shoe_list):
    '''
    Determines lowest-stocked type of shoe.
    Prompt user for re-stocking of shoe.
    Update relevant pair of shoes and save to inventory text file  

    '''

    while True: # Sorts shoe_list in ascending order. Lowest stocked shoe will be in the, shoe_list[0] (first) position 
        sorted_shoe_list = (sorted((shoe_list), key = lambda shoe:shoe.quantity))
        low_stock_shoe = sorted_shoe_list[0]
            
        user_input = input(f"Do you wish to restock {low_stock_shoe.product} (yes/no)?: ")
            
        # Handling of valid 'yes' condition
        if user_input.lower() == "yes":
            while True:
                try:
                    
                    # shoe_restock variable is used to update quantity(attribute) of shoe(object) at shoe_list[0] position 
                    shoe_restock = int(input(f"How much of {low_stock_shoe.product} ({low_stock_shoe.code }) to order from suppliers: "))
                    low_stock_shoe.quantity += shoe_restock
                    print(f"{low_stock_shoe.product} ({low_stock_shoe.code}) has been reordered. The new quantity is at : {low_stock_shoe.quantity} pairs.")
                    
                    # Saving updated shoe(object) to inventory.txt file
                    with open("inventory.txt", "w") as file:
                        for shoe in shoe_list:
                            file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
                            
                    
                    # Exit loop after updating and saving quantity of lowest shoe 
                    break 

                # Handles invalid entry at shoe_restock variable. ie string as opposed to integer         
                except ValueError:
                    print("Numbers only")

        # Handles valid 'no' condition
        elif user_input.lower() == "no":
                print("Noted, no restocking done.")
                break 
         
        else:
            print("Yes or No only...")
    
    
def search_shoe(user_code_search, shoe_list):
    '''
    Allows user to search for a particular shoe using the shoe(objects) code attribute

    Parameters:
        user_code_search (str): ID number for each type of shoe
        shoe_list (list): List of all the Shoe objects(shoes)
    
    Returns:
        Shoe(object): The corresponding shoe provided its been found, else None

    '''

    # Search for shoe based on 'code' attribute.
    # 'lower()' method to eliminate case sensitivity
    for shoe in shoe_list:
        if shoe.code.lower() == user_code_search.lower():
            return shoe
    return None


def value_per_item(shoe_list):    
    '''
    Calculates the total value for each type/class of shoe.
    Determined via the arithmetic product of a shoe's cost and its quantity attributes respectively 
    An objects attributes

    Parameter:  
        shoe_list (list): List of all the objects(shoes)

    Returns:
        value_result (integer): value = (shoe.cost * shoe.quantity)

    '''

    # List used to maintain oder. First element of 'value_result' corresponds to first object
    value_result = []
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        value_result.append(f"The value of the {shoe.product} {(shoe.code)} is equal to R{value}")
    return value_result


def highest_qty(shoe_list):       
    '''
    Determine the most stocked shoe and display it as being up for sale

    Paramters:
    shoe_list(list): List of all the objects(shoes)

    Returns:
        Shoe(object): The shoe object with the highest quantity or None if list is empty
    
    '''     

    # Handle empty
    if not shoe_list:
        return None

    # Initialise first object as 'maximum'
    max_shoe = shoe_list[0]

    # Loop through rest of shoe_list starting at the second object to the end of the lsit
    # Comparing if the corresponding object quantities are greater than the current maximum
    # Update the 'maximum' to the greater shoe quantity each iteration
    for shoe in shoe_list[1:]:

        if max_shoe.quantity < shoe.quantity:

            max_shoe = shoe
    return max_shoe


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

# Load all existing shoes from inventory text file
shoe_list = read_shoes_data()

while True:
        
        print("\n======Nike Inventory Menu=====")
        print("\nSelect an option below via the number")
        print("1. View all the shoes")
        print("2. Capture a new shoe")
        print("3. Restock shoe")
        print("4. Search for shoe via code")
        print("5. Value of shoe(product)")
        print("6. Shoes eligible for sale")
        print("7. Exit program")
      
        while True:
            try:
                user_menu_choice = int(input("Please select an option from the menu: "))
                break
            except ValueError:
                print("Please select a valid option from menu above (numbers 1- 7)")
        
        # Exits program
        if user_menu_choice == 7:
            print("Noted.. Exiting program")
            break

            # Display all the shoes in inventory
        elif user_menu_choice == 1:
            view_all(shoe_list)
      
        elif user_menu_choice == 2:
            # Newly added shoes are displayed
            capture_shoes(shoe_list)
            view_all(shoe_list)

        elif user_menu_choice == 3:
            re_stock(shoe_list)

        elif user_menu_choice == 4:
            # Search for shoe via code
            user_code_search = input("Please enter the code of the shoe: ")
            shoe_code_search_result = search_shoe(user_code_search,shoe_list)
            if shoe_code_search_result:
                print("Shoe Found: ")
                print(shoe_code_search_result)
            else:
                print("\nNo shoe was found with that code. Please try again")

        elif user_menu_choice == 5:
            # Printing value of shoes
            value_of_stock  = value_per_item(shoe_list)
            for value in value_of_stock:
                print(value)

        elif user_menu_choice == 6:
            # Determmining shoe with highest quantity. 
            highest_quantity = highest_qty(shoe_list)
            if highest_quantity:
                sale_price = round(highest_quantity.cost * 0.9,2)
                print(f"The {highest_quantity.product} {(highest_quantity.code)} is on sale at R{sale_price} (original price:{highest_quantity.cost}) for each of the {highest_quantity.quantity} pairs of shoes.")
            else:
                print("\n No shoes found in inventory")
    
        else:
            print("Invalid entry, please try again")
        
    

        


        
    

