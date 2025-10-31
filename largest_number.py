# Program calculates the sum of all the numbers in a list including the given index point

# Function to collect and store integers in list 
def list_fuction():
    """
    Returns:
    list_of_ints (list): A list that will be used to calculate maximum value within list 

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

final_list = list_fuction()

# Initialise variable to serve as counter in update statement
maximum_no = 0

def largest_number(final_list):
    
    """
    Determine the largest number in a list

    Parameters:
    final_list (list): A list used to determine maximum value within the list
    
    Returns:
    maximum number (int): The maximum value within the list

    """

    # If length of list is 1 return element - *used chatgpt to source solution*
    if len(final_list) == 1:                    
        return final_list[0]
    
    # breaking list into smaller pieces getting it closer to base condition.
    else: 
        maximum_no = largest_number(final_list[1:])
        return final_list[0] if final_list[0] > maximum_no else maximum_no # returns first element if first element in list is greater than maximum_no in list 
                                                                           # otherwise return larger element 