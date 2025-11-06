#Program showcasing the total worth of stock in my Cafe.

#Program showcasing the total worth of the stock in my cafe
menu = ["Sandwiches","Muffins", "Coffee", "Matcha","Hennessy"]

#Dictionary of stock value
stock_value_dict = {"Sandwiches": 1200,
              "Muffins": 800,
              "Coffee": 3000,
              "Matcha": 1000,
              "Hennessy": 3000
              }

#Dictionary of prices that appear on menu
price_value_dict =  {"Sandwiches": 35,
              "Muffins": 52,
              "Coffee": 13,
              "Matcha": 81,
              "Hennessy": 92
              }

total_stock_value = {} # dictionary to hold both the key-values respectively

#Loop through each item respectively to get the total stock value. ie stock_value of matcha = stock worth of times * price of matcha on menu
for items in menu:
    total_stock_value[items] = stock_value_dict[items] * price_value_dict[items]

#Stock value of each item
print(total_stock_value)

#Sum of the values - only in total_stock_value, to get the grand total of stock
Total_Stock = sum(total_stock_value.values())
print(f"Total value of stock in cafe is: R{Total_Stock}")