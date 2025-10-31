#Creating dictionaries

int_key_dict = {1:"apple",            #{1:"apple", 2:"banana", 3:mango}
                2:"banana",           # can also be expressed as such
                3:"mango"
                }        

#creating a dictionary from a list
int_key_list = [(1, "apple"), (2, "banana"), (3, "mango")] # note syntax rules 
int_key_dict2 = dict(int_key_list)

# this creates a TUPLE *important*, which is ordered. The order of elemnents is significant as it means something

#THIS IS PATTERN MATCHING
tuple1 = (1, "apple")
key, value = tuple1
print(key) #prints 1
print(value) #prints apple 

#accessing elements in dictionary
profile_dict = {"name": "Chad",
                "surname":"Butter",
                "age": 26,
                "cell_no": "0812345678"
                }
print(profile_dict["age"]) #prints 26
print(profile_dict["name"]) #prints Chad

#can iterate through all the keys & values with your dictionary using .keys & values() method
keys = profile_dict.keys()
values  = profile_dict.values()
print(keys)
print(values)

#changing elements in a dictionary
profile_dict["age"] = 13 # changing age
profile_dict["gender"] = "female" # adding a new key-value pair
print(profile_dict)


#membership testing  - used to test if a KEY exists within a dictionary
double = {1:2,
          2:4,
          3:6,
          4:8
          }
print( 1 in double)