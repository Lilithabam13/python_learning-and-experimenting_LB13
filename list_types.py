#captured friends names in a list of string in variable called 'friends_names'
friends_names = ["Thabo", "Yanga", "Max"]

#print first friend's name
print(friends_names[0])

#print second friend's name
print(friends_names[2])

#print length of list ie. no. of elements
print(len(friends_names))

#capture age of friends in variable called 'friends_ages'
friends_ages = [13, 15, 14]

#print friend's name and age respectively ie. thabo is 13 years old - formatting using f-strings and 
friend_1 = f"{friends_names[0]} is {friends_ages[0]} years old"
friend_2 = f"{friends_names[1]} is {friends_ages[1]} years old"
friend_3 = f"{friends_names[2]} is {friends_ages[2]} years old"
print(friend_1)
print(friend_2)
print(friend_3)