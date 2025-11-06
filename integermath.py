#input the first integer
user_integer1 = int(input("Please enter an integer: "))

#input the second integer
user_integer2 = int(input("Please enter a second integer: "))

#input third integer
user_integer3 = int(input("Please enter a third integer: "))

#organising user inputs in a lsit
user_input = user_integer1, user_integer2, user_integer3

#print the list
print(user_input)

#print the arithmetic sum of the list
print(sum(user_input))

#print the 1st integer minus the 2nd integer
print(user_integer1 - user_integer2)

#multiplication of the 3rd integer & the 1st integer
print(user_integer3 * user_integer1)

#print the sum of the list divided by the 3rd integer
print(sum(user_input)/user_integer3)