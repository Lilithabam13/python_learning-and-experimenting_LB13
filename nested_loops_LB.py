x = 0
y = 0

for x in range(1, 6):
     print("")  
     for y in range(1, 6):
         print(f"{x} * {y} =  {x * y}")
    

# Recap on loops

for i in range(1,14): # Loop counts from 1 to 13
     print(i, end=" ") # 'end= " " ' is way more aesthetic way to display count.


for z in range(5):               # Line 16 - Line 19 is a nested loop whereby we are counting to 13 5 times
    for i in range(1,14): 
        print(i, end=" ")
    print()