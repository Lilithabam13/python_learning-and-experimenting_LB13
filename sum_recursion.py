# Program calculates the sum of all the numbers in a list including the given index point

# Function to collect and store integers in list 
def list_fuction():
    """
    Returns:
    list_of_ints (list): A list that will be used to calculate sum
    """
    
    list_of_ints = []
    
    while True:
        try:
            # Prompting user for valid input. 'no_of_ints' variable must be positive and an integer
            no_of_ints = int(input("Please enter the desired number of integers in your list: "))
            if no_of_ints <= 0:
                print("Positive numbers only")
                continue
            break
        except ValueError:
            print("OOps.. not an integer. Please try again")
    
    # Looping x - number of 'no_of_ints' to store each valid integer
    for _ in range(no_of_ints):
        while True:
            try:
                list_of_ints.append(int(input("Please enter the integers into the list: ")))
                break
            except ValueError:
                print("OOps.. not an integer. Please try again")
    return list_of_ints

# Variable to hold 'final/finished'list
final_list = list_fuction()

# Display final_list
print(final_list)

# Prompt user for index point
try:
    index_point = int(input("Please enter single index point: "))
except ValueError:
    print("OOps.. Numbers only")

# Function calculating sum of list recursively - includes element at index point
def adding_up(final_list,index_point):
    """ 
    Calculate the sum of integers in a list including given index point
    
    Parameters:
    final_list (list): List to sum up
    index point (int): Integer to calculate sum of list up. Must be equal to zero and less than the full len() length of list
        
    Returns:
     sum (int): sum of integers in list including element at given index point

    Raises:
    ValueError if index is negative or greater than the length of list
    """
   
    if index_point == 0:  # Set base condition ie. n = 0    
        return final_list[0]
    
    elif index_point >= len(final_list) or index_point < 0: # index is greater than or negative, rasing an error 
        raise ValueError ("The index you have selected is out of range")
    else:
        return final_list[index_point] + adding_up(final_list,index_point -1) # Set recursive statement

# Displaying the sum of the list including the element at the given index point
print(f"The sum is equal to = {adding_up(final_list,index_point)}")








    