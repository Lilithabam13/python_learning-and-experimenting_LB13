# Initialise variables for specific size of grid

fruit = ["apple","mango", "grapes","litchi"]
veg =   ["brocoli","spinach", "itanga"]
meat_pause =    ["chicken","beef"]

groceries = [fruit,veg,meat_pause]

print(groceries[2][1]) # how to extract specific element via indexing 2d list [2] reps ROW [1] reps column


# Below is a 3 x 2 grid. x being 'by'
number_of_rows = 3
number_of_columns = 2

# create '$' value twice in a list for the colums
# use a loop to do it 3 times for number of rows
grid = ["$" * number_of_columns for _ in range(number_of_rows)]

print(grid)

# Example above prints 2 dollar signs, 3 times in a row. Line 9 says print $ * 2, for loop allows us to do it 3 times thanks to range() 

# Example below is displaying my math marks from term 1 to 4 in grade 12

math_grades = [[71,61,51,66],
               [41,69,72,52],
               [77,66,81,90],
               [81,88,95,100]
               ]
row_index = 0 
for row in math_grades:
    print(f"Term {row_index + 1}: ")
    row_index += 1
    for col in row:
        print(col,end = "% ")
    print()


number_grid = [[1,2,3], # 2D list used to build grid
               [4,5,6], # consists of 4 rows & 3 columns. See horizontal lists as row(s) & vertical lists as column(s)
               [7,8,9],
               [0]
               ]

num = [[2,5,3,7,9],
       [4,1,89,2,10],
       [3,2,6,9,8],
       [12,45,20,50]
       ]
num_max = 0
for row in num:   # this picks each row list one by one. eg. first: [2,5,3,7,9], second:[4,1,89,2,10] etc.
    for col in row: # # loop through elements of row. check each number in that row [2,5,3,7,9], it will pick 2 then 5 then 3 etc.
        if col >=num_max: # compare & update. if current col is greater or eqaul to the current num_nax update. thus finding largest number
            num_max = col
print(num_max)
    

