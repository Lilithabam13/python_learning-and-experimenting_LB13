#The following program calculates the total cost of a holiday in South Africa - including plane tickets, accomadation and car rental services.


print("=============================================")
print(" Welcome to ABC Hotel Group")
print(" Plan the perfect holiday trip with us!")
print("=============================================")

city_flight = {"Johannesburg": 3400,
               "East London": 2420,
               "Nelspruit": 2553,
               "Cape Town": 4200,
               "Upington": 2310
               }

#loop prints index of dictionary starting from 1. User - friendly
for i, city in enumerate(city_flight, start=1):
    print(f"{i}. {city}")

while True:
    print("====================================================================")
    user_input = input("Please enter your travel destination from the list above: \n").title() #string handling method - user_input matches key(s).Eg. nelspruit is Nelspruit 
    if user_input in city_flight :
        
        print(f"You have selected {user_input} as your travel destination") 
        print("=====================================================================")
        break
    else:
        
        print(f"The destination you have selected is not part of our plan. Please select from availabe packages")

num_nights = int(input("Please enter the how many nights you will be staying: \n")) 

print("====================================================================")
rental_days = int(input("Please enter number of days you will be renting a car: \n"))


#Total cost of hotel stay - assuming stay is at same hotel - offering same rates, at diiferent locations.
def hotel_cost(num_nights):
    """
    Calculate cost of hotel.

    Paramters:
    num_nights(integer): input by user - refers to the number of nights user will spend in hotel

    Returns:
    integer:The cost of staying at hotel. 
    R1650 is the standard 'rate' at ABC Hotels across all 5 cities

    """
    H_cost = 1650 * num_nights
    return H_cost

#Total cost of the car rental - *national average*
def car_rental(rental_days):
    """
    Calculate cost of renting car during stay.
    
    Paramters:
    rental_days(integer): input by user - refers to the number of days user intends to rent a car

    Returns:
    integer: The cost of renting car. 
    R420 is the national car rental average in South Africa

    """
    R_cost = 420 * rental_days
    return R_cost

#Total cost of flight - per city
def plane_cost(city_flight):
    """
    Calculate cost of return flight to desired city.
    
    Paramters:
    city_flight(string): input by user - refers to user holiday destination - KEY   in the city_flight dictionary.

    Returns:
    integer: The cost of return flight - correcsponding VALUE in city_flight dictionary.

    """
    if city_flight == "Johannesburg":
        P_cost = 3400
        return P_cost
    elif city_flight == "East London":
        P_cost = 2420
        return P_cost
    elif city_flight == "Nelspruit":
        P_cost = 2553
        return P_cost
    elif city_flight == "Cape Town":
        P_cost = 4200
        return P_cost
    elif city_flight == "Upington":
        P_cost = 2310
        return P_cost

 

#Total cost of holiday
def holiday_cost(num_nights, city_flight, rental_days):
    """
    Calculate total cost of the holiday.
    
    Paramters:
    num_nights(integer), city_flight(integer), rental_days(intgers): refers to the total cost of the holiday.

    Returns:
    integer: sum of hotel_cost, car_rental, plane_cost. 

    """
    total = hotel_cost(num_nights) + car_rental(rental_days) + plane_cost(city_flight)
    return total

#Calcultions for final details - easier to handle
nights = num_nights
rental = car_rental(rental_days)
hotel = hotel_cost(num_nights)
flight = plane_cost(user_input.title())
total_cost = holiday_cost(num_nights,user_input.title(),rental_days)

#Printing of trip details
print("\n------Trip Details------")
print(f"Destination: {user_input}")
print(f"Duration of stay: {nights} nights")
print(f"Rental car cost: R{rental}")
print(f"Return flights cost: R{flight}")
print(f"Stay at ABC hotel cost: R{hotel}")
print(f"----------------------------------------------")
print(f"Total cost of holiday: R {total_cost}")