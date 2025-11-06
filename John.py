#Program below prompts user to guess the name of a dog.
#If the user guesses correctly(John) - a correct statement is returned
#All incorrect guesses are stored and printed once the user guesses correctly


#Store variables in dictionary - specifically chose 'dog_name' as the 'key word(correct anser)' and 
my_dict = { "dog_name": "John",
           "guesses":[] #guesses variable as an empty list to store the user_inputs
           }

while True: #while statement (loop) is ideal iteration because the no. of iterations is unknown (how many times we would have to repeat the user_input)
    user_input = input("Enter the dog's name: ")

#checks if the user's guess is equal to John - from our dictionary key-value pair
    if user_input.upper() == my_dict["dog_name"].upper(): #upper() funct. to eliminate case sensitivity
        print("Correct")
        break #discontinue if user guesses John

#checks if user's guess is not equal to dog. In the event it isn't store each guess into the 'guesses' value in the dictionary as it is a list    
    elif user_input.upper() != my_dict["dog_name"].upper():
        my_dict["guesses"].append(user_input) #append funct to add inputs into list
    
print(f"Incorrect names: {my_dict["guesses"]}") #printing the incorrect names in a list






















# while True:
#     user_input = input("Guess the dog's name: ")   
#     if user_input != "John".upper():
#             user_guesses.append(user_input)
    
#     elif user_input == "John".upper():
#         print("Correct !!")

#     print(user_guesses)


# # while user_guesses == dogs_name.upper():
# #         print("Correct !!")
# #     # if user_input != dogs_name.upper():
# #     #     user_guesses.append(user_input)
# #     #     print(user_guesses)
    
# #     # if user_guesses == dogs_name.upper():
# #     #     print("Correct !!")
        


