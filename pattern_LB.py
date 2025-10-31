#number of rows
counter = 5

#Top half of pattern
for i in range(1, counter *2) :
   if i <= counter:
       print( "x" * i)
#Bottom half of pattern
   else:
       print("x" * (2*counter - i))

#***********************more examples*********************************
# row = 5
# for i in range(1, 2*row):
#     if i <= row:
#         print("*" * i)
#     else:
#         print("*" * (2*row - i))

# row = 5
# for i in range(1, row+1):
#     print("*" * i)

# row = 5
# for i in range(row, 0, -1 ):
#     print("*" * i)