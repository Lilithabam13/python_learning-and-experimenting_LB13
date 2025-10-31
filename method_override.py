# Following program showcases driver elgibilty using OOP fundamentals

# 'Parent class' with 5 instance variable/attributes
class Adult:
    def __init__(self,name,age,hair_colour,eye_colour,legal_driver = True):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour
        self.legal_driver = legal_driver
    
    # method to determine legallity of driver
    def can_drive(self):
        if self.legal_driver == True:
            print(f"{self.name} is old enough to drive")
        
        else:
            print(f"{self.name} is not old enough to drive")
             
# 'Child class' is a subclass of 'Parent class'
class Child(Adult):
    def __init__(self, name, age, hair_colour, eye_colour, legal_driver=False):
        super().__init__(name, age, hair_colour, eye_colour, legal_driver)

# Prompting user for necessary information
while True:
     try:
        name = input("Enter your name:")
        print(".............................\n")
        if not name.isalpha():
            raise ValueError ("Oops letters only")
        
        age = int(input("Enter your age: "))
        print(".............................\n")
        hair_colour = input("Enter your hair colour: ")
        print(".............................")
        eye_colour = input("Enter your eye colour:")
        print(".............................")

        # dictionary to hold the necessary information accordingly
        person_dict = {"name":name,
                       "age":age,
                       "hair_colour":hair_colour,
                       "eye_colour":eye_colour}
        
        print(f"\nThanks {name}, your information has been stored.\n")
        
        # if-else statment to determine whether user is an Adult or not (Child)
        if person_dict["age"] >= 18 :
            person = Adult(**person_dict) # Short version of line 76
        else:
            person = Child(**person_dict) #  Same logic applied

        # calling can_drive method to determine legal status of driver 
        person.can_drive()

        # promoting user as to whether or not they'd like to continue
        to_continue = input("Do you still want to continue ? (y/n): ")
        
        if to_continue.lower()== "y":
            continue
        
        elif to_continue.lower() == "n":
            print("Thanks for participating")
            break
        
        else:
            print("Please try again")
     
     # Error handling. Try block is not executed - user entries are invalid
     except ValueError:
         print("\nOOps... ValueError,\nTry again")      
    

    # extra side not
# person = Adult(person_dict["name"],person_dict["age"],person_dict["hair_colour"],person_dict["eye_colour"])



     



