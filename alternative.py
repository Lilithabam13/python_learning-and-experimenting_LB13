#Get user's input. Removes whitespaces
user_input = input("Please enter a string - to alternate: ").strip()

#Initialise variable to store manipulated string
alternate_string = ""

#Use enumerate() funct to get both the index & letter
for i,char in enumerate(user_input):

#if the index is even - uppercase that specific letter/character     
    if i % 2 == 0 :
        alternate_string += char.upper()

#the odd indexes are the lowercased
    else:
        alternate_string += char.lower()

#+= to add manipulated strings into alternate_variable
print(alternate_string)


#alternate_string is saved under new variable 
new_list = alternate_string.split()

#store string into list to be able to loop through the individual words as oppose to letters
final_new_list = []

#loop through words and not letters
for i, word in  enumerate(new_list):

#Even indexed words are uppercased 
    if i % 2 == 0 :
        final_new_list.append(word.upper())

##Odd indexed words are lowercased
    else:
        final_new_list.append(word.lower())

#Join split words using .join() tool with spaces inbetween ie. " "
str_manipulation = " ".join(final_new_list)
print(str_manipulation)
        