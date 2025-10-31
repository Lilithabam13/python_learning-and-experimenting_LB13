# Example of factorial recursion

# by definition 
# n! = n * (n-1)! , where n >= 1 else if n = 0 then 1 

def fact(n):
    if n >= 1:
        return n * fact(n-1)
    else:
        return 1
    
print(fact(6))
