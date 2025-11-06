#variable to store user's age 
user_age = int(input("Please enter your age: "))

#setting 1st condition (print message if user is over 100 years old)
if user_age >= 100 :
    print("Sorry you're dead")

#setting 2nd condition (user is 40 years or older) 
elif user_age >= 40 :
    print("You're over the hill")

#setting 3rd condition (user is 65 years or older)
elif user_age >= 65 :
     print("Emjoy your retirement!")

#setting 4th condition (user is under 13 years old)
elif user_age < 13 :
     print("You qualify for the kiddie discount")

#setting 5th condition (user is 21 years old)
elif user_age == 21 :
       print("Congrats on your 21st!")

#setting condition, provided previous conditions have not been met (user is 40 years or older)
else :
   print("Age is but a number.")

#!!better code by swapping condition 2 with condition 3. 
#a lot more logical to check for ages between 65 and 99.
#before checking for ages between 40 and 64.
#my coding is still very much single threaded therefore code runs line - by - line