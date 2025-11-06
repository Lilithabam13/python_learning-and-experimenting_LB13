# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.


#1. 'n' the variable below has not been defined.
#2. print() function is missing parentheses, therefore python can not run the following code
#3. Syntax errors 
n = "Welcome to the error program"
print(n)

    # Variables declaring the user's age, casting the str to an int, and printing the result
#1. 'age_Str' variable has been incorrectly stored the '==' refers to equal to (Boolean expression ie. True or False). Not an assignment operator, which was intended 
#2. errors in spacing
#3. print statement has been incorrectly formatted. Missing an 'f-string' tool
#4. logic is inconsistent. you cannot cast letters into string as they already are. would be best to 
#5.combination of error types including a syntax error,which would then become a runtime error due to the trying to cast letters into integers
age = 24 
print(f"I'm {age} years old.")

    # Variables declaring additional years and printing the total years of age
#1.'3' is an integer therefore it does not need quotation marks
#2.'age' variable has not been defined
#3.'answer_years' is not a variable. It should be 'total_years'
#4.print statement has missing parentheses as well as incorect formatting/casting
#5.cast integer 'total_years' into string
#6.Errors included Syntax, Runtime and Logical errors
years_from_now = 3
age = 10
total_years = age + years_from_now
print("The total number of years: " + str(total_years))

# Variable to calculate the total number of months from the given number of years and printing the result
#1.'total' variable has not been defined
#2.print statement has missing parentheses and has been formatted incorrectly
#3.Errors included Syntax as well as Runtime errors

total = 27.5
total_months = total * 12
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old ")

#HINT, 330 months is the correct answer

