import math

#The following Python program is a Finance Calculator, allowing prospective users to access an: Investment Calculator and a Home Loan Repayment Calculator.
#Covers if-elif-else statements, variables, arithmetic operations,data types, string manipulation(formatting) and different tools and functions ie. .upper() and round()

#displaying the user's options
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")

#creating a space between the text for legibility
print("")

#capturing the user's input via input function under 'user_input' variable
user_input = input("Enter either 'investment' or 'bond' from the menu above to proceed:")

#setting a condition ie. user selects 'investment'. Using the upper() tool to ensure the user's input is caputured regardless of the casing ie. inVestMent
if user_input.upper() == "INVESTMENT":

#*capturing relevant information required to do the calculations*

#float data type used to capture the user's Deposit in (Rands). Using this data type is ideal when storing money 
    investment_deposit = float(input("Please enter your inital deposit amount in rands: "))

#float data type ideal to capture (Interest Rate) as is can be expressed as a fraction
    investment_interest_rate = float(input("Enter the interest rate (as a percentage): "))

#used float data type as (Years) can be expressed as a fraction/decimal ie 2.5 years - just covering my bases
    investment_period = float(input("Please enter the number of years: "))

#prompting the user to choose on how to calculate their investment. Via simple or compound interest
    interest = input("Do you want to calculate your investment on a 'simple' or 'compound' interest: ")

#setting the first condition (in the event user elects to calculate an investment) ie. user's selects to calculate their investment via Simple Interrest    
    if interest == "simple":

#formula to calculate investment via simple interest - round() function to round off 'A' to 2 decimal places
        A = round(investment_deposit * (1 + (investment_interest_rate/100) * investment_period),2)
        A_final_statement = f"Total investment over the selected period is R{A}"
        print(A_final_statement)

#setting second condition (in the event user elects to calculate an investment) ie. user's opts to calculate their investment using Compound Interest   
    elif interest == "compound":

#formula to calculate investment via compound interest - round() function to round off 'A' to 2 decimal places
        A = round(investment_deposit * math.pow((1+(investment_interest_rate/100)),investment_period),2)
       #A_rounded = round(A, 2) - why did this not work

#formatting 'final_investment_statement' variable using f-strings to avoid having to cast 'A' varible using str()
        final_investment_statement = f"Total investment over the selected period is R{A}"

#displaying the user's Investment according to their specifics
        print(final_investment_statement)

#setting third condition ie. in the event user's input has nothing to do with the specifics of the program   
    else:
        print("Invalid entry, please re-run the calculator")

#setting a condition ie. user selects 'bond'. Using the upper() tool to ensure the user's input is captured regardless of the casing ie. BonD
elif user_input.upper() =="BOND":

#float data type used to capture the user's property value in (Rands). Preferred data type to store money
    property_value = float(input("Please enter the current property value: "))

#float data type ideal to capture (Interest Rate) as is can be expressed as a fraction
    interest_rate = float(input("Please enter the interest rate: "))/100

#used float data type to cpature (Months) - integer data type is most appropriate. But what happens it the event user expresses 'repayment_period' as a fraction/decimal ie 72.5 months - I may be overthinking    
    repayment_period = round(float(input("Please enter the number total repayment period (in months): ")),0)

#formula to calculate bond repayment - round() function to round off 'repayment' to 2 decimal places
#used chatgpt to fix my comma error as python interpreted the code as a tuple 
    repayment = round (( interest_rate / 12 * property_value ) / ( 1 - (1 + interest_rate / 12 ) ** ( - repayment_period )),2)

#is there a way to print the repayment_period in the statement without the decimal. May be contradicting myself *just asking*
    final_bond_statement = f"Total bond repayment over {repayment_period} months, is R{repayment}"
    print(final_bond_statement)

#setting condition ie. in the event user's input has nothing to do with the specifics of the program ('neither investment nor 'bond' selection)   
else:
    print("Invalid entry, please re-run the calculator.")


# * Wow, I am defeated ☺☺☺  - ready for more *. I feel as though this maybe too much explaining - but I'll wait to hear your feedback.
#Regards,
