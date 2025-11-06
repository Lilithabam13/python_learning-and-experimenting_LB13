numbers = []

while True :
   
   user_input = int(input("Please enter a numnber: "))
   if user_input == -1:
     break 
   
   if user_input == 0:
     continue    
   
numbers.append(user_input)
print(sum(numbers)/len(numbers))

    
