food_item = ["Lasagna", "is", "dogs", "cats", "and", "monkeys"] # created a list
print(food_item[1:3]) # slicing the list to extract specific elements
print(food_item[0]) #indexing to extract specific element
food_item[0] = "Salad" #change element within list
print(food_item)
food_item.append("mangos") #adding an element to the list
print(food_item)
del food_item[4] # deleting an element from list
print(food_item)

#Nested list example

a = [1,2,3]
b = [4,5,6]
c = [a,b,"tea", 16] # Nested list
c.remove(a) #following is referred to as a list method - there are many others See pg.3 & online for more
print(c)

#Slicing a list to make a copy

a = [1,2,3]
e = a[:]
e[0] = 13
print(a)
print(e) #shows the current state of list a even though we only modified list e.
         #created a shallow copy
    

#Using copy module - best to use when list contains inner list/s

import copy

f = [[1,2,3],[4,5,6]]
g = f[:]
h = copy.deepcopy(f) 
g[0][1] = 10 #changes positon [0][1] in both f & g
h[1][1] = 13
print(f)
print(g)
print(h)


#Looping through items - to access each element

food = ["Chicken", "Pizza", "Cabbage", "Cheese"]
i = 0
while i < len(food): # run from index 0 to index 1 less than the list length
    print(food[i]) # print element/item at that position
    i+=1 # increment i - increase (by fixed value )of i by 1. chicken then pizza then cabbage 

for i in food: # loop through each item on food list
    print(i) # print each item

#Both do the same operation -- just different methods


#List comprehension

#following is an example of list comprehension *Note the structure - expression followed by for statement inside square brackets*
num_list = ["1","2","3","4","5"] #string of integers
new_num_list = [int(element)*2 for element in num_list] #each element is cast into an intger & multiplied by 2.
print(new_num_list)