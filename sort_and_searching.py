# Program showcasing various sorting and searching algorithms

dataset = [27,-3,4,5,35,2,1,-40,7,18,9,-1,16,100]
target = 9

# Linear search works for the list above becasue the list is already sorted 
def sequential_search(target,dataset):
    """
    Perform sequential search on sorted list to find target item
    
    Parameters:
        target (int): number we are searching for within dataset
        dataset (list): sorted list of numbers

    Returns:
        int: index of target number within index     
    """
    for index,value in enumerate(dataset):
        if value == target:
            return index
        
    return None



# Census data within a small farming town
def insertion_sort(dataset):
    """
    Perform insertion sort on unsorted list
    
    Parameters:
        dataset (list): unsorted list of numbers

    Returns:
        sorted_dataset (list): sorted list of numbers in ascending order     
    """
    for i in range(1, len(dataset)):
        j = i
        while dataset[j-1] > dataset[j] and j > 0:
            dataset[j-1], dataset[j] = dataset[j], dataset[j-1] 
            j -= 1
    return dataset


# Can be used to find height in a class of students
def binary_search(target,sorted_dataset):
    """
    Perform binary search on sorted list to find number 9 within 
        sorted_dataset
    
    Parameters:
        target (int): number we are searching for within dataset
        sorted_dataset (list): sorted list of numbers in ascending order

    Returns:
        midpoint (int): index of target number within dataset     
    """

    low, high = 0, len(sorted_dataset) - 1
    while high > low:
        midpoint = (low + high) // 2
        if sorted_dataset[midpoint] == target:
            return midpoint
        
        elif sorted_dataset[midpoint] < target:
            low = midpoint + 1
        
        else:
            high = midpoint - 1
    
    return None


##############################
# Example usage

# sequential_search
print(sequential_search(target,dataset))

# insertion_sort
sorted_dataset = insertion_sort(dataset)
print(sorted_dataset)


# binary_search
result = binary_search(target,sorted_dataset)
if result is not None:
    print(f"item {target} is at index {result}")
else:
    print(f"item {target} could not be found in list")



