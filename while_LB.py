
#List to store input variables
x = []

while True:
 user_input = int(input("Enter a number (press -1, to calculate average): "))

 if user_input == -1:
    break

 elif user_input == 0 :
   continue 
 
 #add user input into list using append() function
 x.append(user_input)

#Computing the average of user lsit
avg_of_valid_no = round(sum(x)/len(x),2)
print(avg_of_valid_no)