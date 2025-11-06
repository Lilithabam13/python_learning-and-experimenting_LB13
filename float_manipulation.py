#Following program illustrates operations of statistics module and use of built-in fuctions
#How it can be incorporated in basic statistics

import statistics as S

#variable to store data
data = []

#Prompting user to enter 10 numbers. Will be stored in empty 'data' list
for i in range(1, 11):
    user_input = float(input("Please enter a number: "))
    data.append(user_input)

#Legibility    
print("\nData entered:",data)

#Calculations using round() tool as well as built-in functions. Not to mention combining functions with methods
sum_of_data = round(sum(data),2)
max_index = data.index(max(data))
min_index = data.index(min(data))
avg_temp = round(S.mean(data),2)
temp_median = round(S.median(data),2)

#Legibility
print("\nResults")
#Printing the results - using f strings
print(f"The total of the dataset is: {sum_of_data}")
print(f"The index of the maximum is: {max_index}")
print(f"The index of the minimum is: {min_index}")
print(f"The average of the dataset is: {avg_temp}")
print(f"The median of the given dataset is: {temp_median}")

