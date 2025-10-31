# Creating Robot CLASS
class Robot:
    def __init__(self,name,weight,colour): # constructor, defining our Class (DEFINNG HOW OUR OBJECT IS INITIALIZED). Currently has 3 instance variables
        self.name = name
        self.weight = weight
        self.colour = colour

    def say_hi(self): # this is an example of creating a method (what our CLASS is able to do)
        print(f"Hello my name is {self.name}\n and I'm {self.colour} in colour") # 

    
robot1 = Robot("Tom",92,"Lime") # this is an example of creating an object - better yet defining an object

robot1.say_hi() # this is an example of method calling

# Method overriding - same method(funct) name
class Monk:
    def life(self):
        print("I sold my ferrari")

class Lawyer(Monk):
    def life(self):
        print("Love that for you")

famous_book = Lawyer()

famous_book.life()


# Inheritance using super() function

class Computer:
    def __init__(self,computer,ram,ssd):
        self.computer = computer
        self.ram = ram
        self.ssd = ssd

class Laptop(Computer):
    def __init__(self, computer, ram, ssd, model):
        super().__init__(computer, ram, ssd)
        self.model = model

Laptop1 = Laptop("Apple", 8, 513, "Macbook 5000")

print(f"Make: {Laptop1.computer}")
print(f"Model: {Laptop1.model}")
print(f"RAM: {Laptop1.ram}")
print(f"SSD: {Laptop1.ssd}")