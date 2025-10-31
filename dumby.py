import math

property_value = float(input("Please enter the current property value: "))
interest_rate = float(input("Please enter the annual interest rate (%): ")) / 100
repayment_period = int(input("Please enter the total repayment period (in months): "))

# Monthly bond repayment formula
repayment = round(
    (interest_rate / 12 * property_value) / ((1 + interest_rate / 12) ** (-repayment_period)),
    2
)

print("Your monthly bond repayment is R" + str(repayment))


