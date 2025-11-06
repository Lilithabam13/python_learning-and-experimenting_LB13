# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.
#1.'animal' variable has not been defined properly, 'Lion' since its a string should be in quotation marks.
#2. The logic in 'full_spec' variable is inconsistent. It should read "This is a {animal_type}. It is a {animal} and it has {number_of_teeth} teeth".
#3. 'full_spec' variable is missing 'f-string' at the start of the sentence to correctly format the argument 
#4. print function in line 14 has missing parentheses
#5. Errors in this program included Syntax errors, as well as a Logical error - as the original sentence did not make any sense

animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal_type}. It is a {animal} and it has {number_of_teeth} teeth"

print(full_spec)

