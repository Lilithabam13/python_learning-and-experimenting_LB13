# 'Everything in python is an object of a class'
# Class is the blueprint - plan
# Object is the product of that plan/class

# Therefore lists,strings,dict,functions,numbers are all objects of data classes

my_list = [1,2,3]  # object of built-in list class
my_str = "DK13" # object of built-in str class

my_dict = {"Music": "Babyface Ray",  # object of built-in dictionary class
           "Team": "Spurs",
           "No.":13
           }

my_num = 13 # object of built-in int(float,complex etc.) class

def my_funct(x=1,y=3): # object of function class - because i defined it 
    return x - y

# print() or len() # object of built-in function or method class

# A class stores properties, functions called methods which run programmicly to return the class properties

# Eg. 'Str' Class 
# has a value which is the string & methods such as upper(), lower(), split() etc.

# Below is an example of defining a class in Python

class Student():
    def __init__(self,age,name,gender,grades): # Constructor - answers question of what we need to define our class ie. a student's name , age, gender , grades ,student id etc.
        self.age = age # age passed in the constructor as argument is equal to the age of our object (student)
        self.name = name # same logic applied 
        self.gender = gender # same logic applied
        self.grades = grades

# Creating a method from a class example - defined under Student class
    
    def compute_avg(self):
        average = sum(self.grades)/len(self.grades)
        print(f"The average grade of {self.name} is {average}")

# Creating objects from our class - example of 2 objects of Student class called Lutho & Amy

Lutho  = Student(20,"Lutho Xaba", "Female",[13,26])
Amy = Student(24, "Amy Win", "Female", [13,9])

Lutho.compute_avg() # Method call only after defining objects

# Instance vs Class variables - See Pg 8-9
# Instance refers to variable unique to each object - house number
# Class refers to shared variables between objects - zip code


# Example of changing attribute value outside object
class Wolf:
    classification = "canine"
    habitat = "forest"
    is_sleeping = False

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_sleep_state(self):
        if self.is_sleeping == False:
            return self.name + " is awake"
        else:
            return self.name + " is sleeping"

silver_tooth = Wolf("Silver Tooth", 6)
print(silver_tooth.show_sleep_state())

silver_tooth.is_sleeping = True
print(silver_tooth.show_sleep_state())
