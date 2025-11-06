#user input - to capture thr athlete times
user_swimming_time = int(input("Please enter your swimmng time: "))
user_running_time = int(input("Please enter your running time: "))
user_cycling_time = int(input("Please enter your time: "))

#sum of user times
user_time = user_swimming_time + user_running_time + user_cycling_time 
print("Total time taken for the triathlon: " + str(user_time) + " " + "minutes")

#setting condition 1 for qualifying time between 0 - 100 mins
if user_time <= 100 :
   print("Award: Provincail colours")

#setting condition 2 for qualifying time between 101 - 105 mins
elif (user_time < 100) or (user_time <= 105):
   print("Award: Provincial half colours")

#setting condition 3 for qualifying time between 106 - 110 mins
elif (user_time > 105) and (user_time <= 110):
   print("Award: Provincial scroll")

#setting condition when none of the conditions have been met ie. qualifying time 111+ mins
else:
   print("No award")