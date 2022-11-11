import os
"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

import numbers
from stringprep import in_table_c11_c12
from data import warehouse1, warehouse2

# YOUR CODE STARTS HERE

    # Get the user name
user_name = input("Please state your username: ")
    # Greet the user
print ("Welcome to the warehouse system,", user_name)
    # Show the menu and ask to pick a choice
while True:
    menu = int(input ("1. List items by warehouse \n2. Search an item and place an order \n3. Quit\n"))
    
    # If they pick 1
    if menu == 1:
        print (" \n Warehouse 1 \n")
        for count, i in enumerate(warehouse1):
            print (count+1 , i)
        print (" \n warehouse 2 \n")
        for count, i in enumerate(warehouse2):
            print (count+1 , i)
    # Else, if they pick 2
    elif menu == 2:
        # clear the terminal with os
        os.system("clear")
        item_name = input ("Please state the Item you are searching for: ")
        item_name = item_name.capitalize()
        if item_name in warehouse1 and item_name in warehouse2:
            print (item_name, "Is in both warehouses")
            i_1 = 0
            i_2 = 0
            for i in warehouse1:
                if i == item_name:
                    i_1 += 1
            for i in warehouse2:
                if i == item_name:
                    i_2 += 1
            if i_1 < i_2:
                print ("Warehouse 2 has more in Stock")
            elif i_1 > i_2:
                print ("Warehouse 1 has more in Stock")
            else:
                print ("Equal distribution")
            number = i_1 + i_2
            print ("There are ", number, "Pieces in Stock")
            print (i_1, "in Warehouse 1")
            print (i_2, "in Warehouse 2")
        elif item_name in warehouse1:
            number = 0
            for i in warehouse1:
                if i == item_name:
                    number += 1
            print ("There are ", number, "Pieces in Stock")
            print (item_name, "is in Warehouse 1")
        elif item_name in warehouse2:
            number = 0
            for i in warehouse2:
                if i == item_name:
                    number += 1
            print ("There are ", number, "Pieces in Stock")
            print (item_name, "is in Warehouse 2")
        else:
            print ("Not in Stock")
            number = 0
        
        order = input ("Do you want to place an order? (Y/N)")
        if order == "Y":
            order_number = int(input ("How much do you want to order?"))
            if order_number < number:
                print ("The order of", order_number, "Pieces of", item_name, "is placed")
            elif order_number > number or order_number == number:
                max_order = (input("We have that number or your order is even exceeding our storage. Do you want to place an order for maximum available? (Y/N)"))
                if max_order == "Y":
                    print("The maximum amount of", item_name, "has been ordered!")
                
        

    # Else, if they pick 3
    elif menu == 3:
        break

    # Else
    else: print("Invalid input, try 1, 2, or 3")
    # Thank the user for the visit
print ("Thank you for the visit, ", user_name)