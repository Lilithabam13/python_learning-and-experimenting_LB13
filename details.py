#Task 1
#The folowing program will get the name, age, house number and street name from a user

#user's name
user_name = input("Please enter your name and surname: ")

#user's age
user_age = int(input("Please enter your age: "))

#user's house no.
user_house_number = int(input("Please enter your house number: "))

#user's street name
user_street_name = input("Please enter your street address: ")

#tried two different methods
print("This is {}. He is {} and lives at house number {} on {}." .format(user_name, user_age, user_house_number, user_street_name))
#print("This is " + user_name + "." + " He is " + str(user_age) + " and he lives at " + str(user_house_number) + " on " + user_street_name)


