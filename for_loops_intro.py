#another way of printing the list using for loops - print each element of the list
#a = ["pear","apple","mango"]
#for each_element in a:
#    print(each_element)

#correct syntax when using for loops
#b = [20, 10, 13]
#for i in b:
#    print(i)

#how to cycle through each element of the list adding an additional variable - print statement must be out the loop to display the full total
#c = [20, 10, 13]
#total = 0
#for i in c:
   # total = total + i
#print(total)

#in the event you wanted to print all the numbers from 1 to 5. use range() function
#for i in list(range(1, 6)): # this print all no. starting from 1 to 6 EXCLUDING 6 into a list
#print(i)

total2 = 0
for i in range(1, 6):
    total2 += i
print(total2)

#range(1, 6) = 1, 2, 3, 4, 5
#start: total2 = 0 - initial value of total2
# Add 1 - total2  = 1
# Add 2 - total2  = 3
# Add 3 - total2  = 6
# Add 4 - total2  = 10
# Add 5 - total2  = 15

#task 1 -  print sum no.s that are multiples of 4 in range of no.s 1 - 50.
total3 = 0
for i in range(1, 51):
    if i % 4 == 0 : #using modulus operator - anything that divides into 4 perfectly with no remainder is a mutlple of 4
        total3 += i
print(total3)

#task 2 - compute sum of numbers that are multiples of 3, 5 & 9 less than 100.
total4 = 0

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0 and i % 9== 0: # if is a multiple of 3, 5 & 9
        total4 += i                            # calculate the sum of those numbers

print(f"The sum of all the multiples of 3, 5, and 9 less than 100 is {total4}")

#compute all the multilples of 3 & 5 less than 100

total5 = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0 :
        total5 += i
print(total5)