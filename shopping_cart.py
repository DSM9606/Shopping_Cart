

import math 
import time
from datetime import date
import datetime
e = datetime.datetime.now()


print(" ")
print(" ")
print("--------------------------------------------------")
print("--------------------------------------------------")
print(" ")
print("       Dan's East Fulton St. Grocery Store")
print("            www.dansgrocerystore.com")
print(" ")
print("         Digital Shopping Cart Receipt ")


print("--------------------------------------------------")
print("--------------------------------------------------")
print(" ")
print("STEP 1: Input Product ID #1 - #20 + ENTER")
print("STEP 2: Type 'DONE' + ENTER when Product Input Complete")
print(" ")
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] 

# based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71



total_price = 0
selected_ids = []



while True: #information capture / input
  
    selected_id = input("     Please input a product identifier: ") #This code prompts the user for a selected identifier, and then we used that selected identifier to look up all of the products matching that identifier 
    if selected_id == "DONE":
        print(" ")
        print("--------------------------------------------------")
        print("--------------------------------------------------")
        print(" ")
        break
    else:                  
        print(" ")
        print(" ")
        selected_ids.append(selected_id)
   
    #else: selected_id =
        #print("d")
        
         #matching_products = [p for p in products if str(p["id"]) == str(selected_id)] #This allows you to look up products matching an identifier
        #matching_product = matching_products[0] 
        #total_price = total_price + matching_product["price"]
        #print("SELECTED PRODUCT: " + matching_product["name"] + " " + str(matching_product["price"]))

    #else if selected_id <> "DONE" or matching_product:
        #selected_id = input("Please input a product identifier: ")

#This above code is from Professor Rosetti in "Shopping Cart" Project Walkthrough 
#https://www.youtube.com/watch?v=3BaGb-1cIr0

#print(selected_id!="1" or "2" or "3")
    
    #print("invalid choice")




print(" ")
print(" ")
print(" ")
print("       Dan's East Fulton St. Grocery Store")
print("            www.dansgrocerystore.com")
print(" ")
print("       PLEASE REVIEW YOUR DIGITAL RECEIPT ")
print(" ")
print("--------------------------------------------------")
print("--------------------------------------------------")
print(" ")
print("  CHECKOUT TIME: ", e.strftime("%a, %b %d, %Y, %I:%M %p"))
print(" ")
print("--------------------------------------------------")
print("--------------------------------------------------")
print(" ")

print("               SELECTED PRODUCTS: ")
print(" ")

for selected_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)] #This allows you to look up products matching an identifier
    matching_product = matching_products[0] 
    total_price = (total_price + matching_product["price"])
    print ("    " + "(" + str(to_usd(matching_product["price"])) + ") " + matching_product["name"])
        #selected_ids.append(selected_id)
#print(selected_ids) 

#for selected_id in expressionline
#I got this time code from https://phoenixnap.com/kb/get-current-date-time-python

print(" ")
print("--------------------------------------------------")
print("--------------------------------------------------")
print(" ")
#import math # i learned how to do two decimal places with this code https://java2blog.com/format-a-float-to-two-decimal-places/
print("              Subtotal: " + to_usd(total_price) )
print(" ")
print("             Sales Tax: " + to_usd((total_price*.0875)))
print(" ")
print("                 Total: " + to_usd(total_price*.0875+total_price))
print(" ")
print("--------------------------------------------------")

#This above code is from Professor Rosetti @ 40:38/51:11
#https://www.youtube.com/watch?v=3BaGb-1cIr0


#This above code is from Professor Rosetti @ 40:38/51:11
#https://www.youtube.com/watch?v=3BaGb-1cIr0


#information display / output

print("--------------------------------------------------")
print(" ")
print("         Thank You For Shopping With Dan")
print("               Please Come Again!!")
print(" ")
print("      Dan's East Fulton St. Grocery Store")
print(" ")
print("         42 Fulton St. New York NY 10004")
print(" ")
print("--------------------------------------------------")
print("--------------------------------------------------")
print(" ")
print("            www.dansgrocerystore.com")
print("              Phone: (212) 444-4444")
print("   ")

import datetime
now = datetime.datetime.now()
print("      CHECKOUT: ", e.strftime("%a, %b %d, %Y, %I:%M %p"))
print(" Checkout Long Time:  ", (str(now))) #this code was from a googled website
#https://www.tutorialspoint.com/How-to-print-current-date-and-time-using-Python
print(" ")
print("--------------------------------------------------")
print("--------------------------------------------------")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")

             





#def to_usd(my_price):
    # """
    # Converts a numeric value to usd-formatted string, for printing and display purposes.

    # Param: my_price (int or float) like 4000.444444

    # Example: to_usd(4000.444444)

    # Returns: $4,000.44
    # """
    # return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output

#print(products) #This code prints all the products (We used this at the beginning of the tutorial)


#A grocery store name of your choice
#A grocery store phone number and/or website URL and/or address of choice
#The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2020-02-07 03:54 PM)
#The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $3.50, etc.)
#The total cost of all shopping cart items (i.e. the "subtotal"), formatted as US dollars and cents (e.g. $19.47), calculated as the sum of their prices
#The amount of tax owed (e.g. $1.70), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax)
#The total amount owed, formatted as US dollars and cents (e.g. $21.17), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
#A friendly message thanking the customer and/or encouraging the customer to shop again