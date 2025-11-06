#introduced 'user_sentence' variable
user_sentence = input("Please enter a sentence: ")

#assigned str_manip variable value of 'user_sentence', as per task
str_manip = user_sentence

#print the length of characters/elements in the sentence using len() function
print(len(str_manip))

#found the last letter of 'str_manip' via indexing where [-1] is holds the position of the last character, reading from left to right
last_letter =str_manip[-1]

#print the last letter variable
print(last_letter)

#new variable called 'replaced_last_letter' is equal to replacing the 'last_letter' with an @ symbol
replaced_last_letter = last_letter.replace(last_letter, "@")

#new variable is equal to finding the postion of the occurence of 'last_letter' variable within the 'str_manip' value
trying_to_find_ll = str_manip.find(last_letter)
print(trying_to_find_ll)

#replacing the occurence of the 'last_letter' (character) with an '@' symbol ie "the cat" WILL NOW BECOME '@he ca@'
xx = str_manip.replace(last_letter, "@")
print(xx)

#replaced the "@" symbol with the 'last_letter' uunder new variable
new_str_manip = xx.replace("@", last_letter)
print(new_str_manip)

#introduced new variable called 'last_three_letters' and printed the last 3 letters
last_three_letters = new_str_manip[-3:]
print(last_three_letters)

#print the 'last_three_letters' backwards
last_three_letters_backwards = last_three_letters[::-1]
print(last_three_letters_backwards)

#print the first 3 characters
first_three_letters_ = str_manip[0:3]
print(first_three_letters_)

#print the last 2 characters
last_two_letters = str_manip[-2:]
print(last_two_letters)

#print five letter word via concation of variables
five_letter_word = first_three_letters_ + last_two_letters
print(five_letter_word)