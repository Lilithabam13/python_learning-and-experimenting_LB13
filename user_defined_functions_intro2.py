def multiply(num1 = 1, num2 = 3):
    total = num1 * num2
    print(f"{num1} * {num2} = {total}")

multiply_test = multiply() #both default values are used
multiply_test = multiply(2) # first argument (num1) is overwritten - due to the order
multiply_test = multiply(4,6) # both arguments are overwritten
multiply_test = multiply(num2= 6,num1= 6) # keywords used to get around the order 