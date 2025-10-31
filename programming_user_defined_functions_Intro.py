def add_one(x): # user defined function called 'add_one'.It takes the parameter (x) as an input. 
    y = x + 1   # A Parameter is variable that is declared in a function definition. 
    return y    # Paramters store data needed to perform the logic the function specifies.
                # Code indented is called the logic of the function and defines what happens when the fuction is called 
    
                #CODE ABOVE 
                #'add_one' is the name of function
                # 'y' is the expression while ' x + 1' is the logic or what happens when parameter 'x' is called
#Think of a funtion as a placeholder
# Print examle
print(add_one(5)) # Output is 6

#Inside calculaton
k = add_one(13) * 2 # K is equal to 28

#Variable
lb = add_one(12) # lb is equal to 13

#More examples

def greet(name): # function name is 'greet' takes 'name' and prints personalised greeting
    print(f'My name its {name}!')
greet("Warabile") #Will print "My name its Warabile" in console

def add(a, b): # defined 'add' function as the sum of 2 variables passed in arguments
    return a + b # function has been defined at this point

result = add(3,10)  # introducing function to new variable with 2 parmeters (arguments)
print(result)  # printing 'result'

#Use PRINT to show data. use RETURN to when we want function result saved/reused or combined with other logic

#Scope - refers to a function's "one-way glass" approach. Function can see out, but no one can see in.

def adding(a, b): # SEE PG.7
    total = a + b
    return (description + str(total))

x =   2
y = 3
description  = "Total: "
sum = adding(x, y)
print(sum)

# Default values - we can assign default values to our parameters/arguments
def multiply( num1, num2 = 3): #default value of num2 has been set to 3
    total = num1 * num2
    print(f"{num1} * {num2} = {total}") #as it stands this output num1 * 3

#Introduce new variable 
times_3 = multiply(1) # we dont have to include second arguement as its already been set
                      # if we did the same operation but instead removed default value of num2. Program would crash SEE PAGE 9
# def multiply( num1, num2): #program would crash
#     total =  num1 * num2
#     print(f"{num1} * {num2} = {total}")

# times_4 = multiply(1)   # As num2 has not been defined

# times_12 = multiply(num1=3,num2=4)- this not only overides the value of num2. Its also introduces keywords meaning the order in which we write our arguments has no effect

#See Pg.10