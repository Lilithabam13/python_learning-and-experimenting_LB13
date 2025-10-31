# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": "d'oh!",  # Value had not been closed properly. Included comma in value, which is used to seperate each key-vaule pair.
                         "maggie": "(Pacifier Suck)"
                         }


# Function to print dictionary values given the keys
def print_values_of(simpson_catch_phrases): # created a link between the dictionary and the function via consistent naming of the variables
    for phrase in simpson_catch_phrases.values(): # printing each value in the dictionary using 'values' method  
        print(phrase)

print(print_values_of(simpson_catch_phrases)) # missing print statement. Final dictionary took 4 arguemnts as opposed to 2


'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

