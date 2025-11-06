#following program is a SIMPLE vehicle financing calculator

import math

#Storing of necessary information 
user_name_and_surname = input("Please enter your name and surname: ")
valuation_of_car = float(input("Please enter the value of the vehicle: R "))
deposit = float(input("Please enter the deposit (optional): R "))
repayment_period = int(input("Please enter the repayment period (in years): "))
interest_rate = float(input("The interest rate (%): "))


while True:
#Defining the amortization fomrula
    P = valuation_of_car - deposit
    r = (interest_rate / 100) / 12
    n = repayment_period * 12
    
    M = round((P * r * (1 + r)*n) / ((1 + r)**n -1),2)


    print("..................................................")
    print(f"Hello {user_name_and_surname}, here are your finance details: ")
    print(f"Loan Amount: R{P}")
    print(f"Monthly repayment = R{M}")
    print("..................................................")
#print statement
    break