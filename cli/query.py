import os
import datetime
"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import stock
def menu():
    user_name = input("Please state your username: ")
    # Greet the user
    print ("Welcome to the warehouse system,", user_name)
    # Show the menu and ask to pick a choice
    while True:
        menu = int(input ("1. List items by warehouse \n2. Search an item and place an order\n3. Search by Category\n4. Quit"))
        if menu == 1:
            list_all()
        elif menu == 2:
            search_item()
        elif menu == 3:
            search_category()
        elif menu == 4:
            break
        else: print("Invalid input, try 1, 2, or 3")
    # Thank the user for the visit
    print ("Thank you for the visit, ", user_name)

def list_all():
    os.system("clear")
    print (" \n Warehouse 1 \n")
    total_items1 = []
    for i in stock:
        if i["warehouse"] == 1:
            total_items1.append(i)
            print (f"{total_items1.index(i) + 1}. {i['state']} {i['category']}")                
    print (" \n warehouse 2 \n")
    total_items2 = []
    for i in stock:
        if i["warehouse"] == 2:
            total_items2.append(i)
            print (f"{total_items2.index(i) + 1}. {i['state']} {i['category']}")
    print (f"Total items in warehouse 1: {len(total_items1)}\nTotal items in warehouse 2: {len(total_items2)}")

def search_item():
    os.system("clear")
    item_name = input ("Please state the Item you are searching for: ")
    warehouse1 = []
    warehouse2 = []
    for i in range(len(stock)):
        if stock[i]["state"].upper() in item_name.upper() and stock[i]["category"].upper() in item_name.upper() and stock[i]["warehouse"] ==1:
            warehouse1.append(stock[i])
        elif stock[i]["state"].upper() in item_name.upper() and stock[i]["category"].upper() in item_name.upper() and stock[i]["warehouse"] ==2:
            warehouse2.append(stock[i])
    if len(warehouse1) > 0 and len(warehouse2) > 0:
        print (item_name, "Is in both warehouses")
        #print(f"{len(warehouse1)} items in warehouse 1 and {len(warehouse2)} items in warehouse 2.")
                
        if len(warehouse1) < len(warehouse2):
            print ("Warehouse 2 has more in Stock")
        elif len(warehouse1) > len(warehouse2):
            print ("Warehouse 1 has more in Stock")
        else:
            print ("Equal distribution")
        number = len(warehouse1) + len(warehouse2)
        print ("There are ", number, "Pieces in Stock")
        print (len(warehouse1), "in Warehouse 1")
        print (len(warehouse2), "in Warehouse 2")
    elif len(warehouse1) > 0 and len(warehouse2) == 0:
        print ("There are ", len(warehouse1), "Pieces in Stock")
        print (item_name, "is in Warehouse 1")
    elif len(warehouse2) > 0 and len(warehouse1) == 0:
        print ("There are ", len(warehouse2), "Pieces in Stock")
        print (item_name, "is in Warehouse 2")
    else:
        print ("Not in Stock")
    print("Location:")
    for i in warehouse1:
        delta = datetime.datetime.now() - datetime.datetime.strptime(i["date_of_stock"],"%Y-%m-%d %H:%M:%S")
        print(f"- Warehouse 1 (in stock for {delta.days} days)")
    for i in warehouse2:
        delta = datetime.datetime.now() - datetime.datetime.strptime(i["date_of_stock"],"%Y-%m-%d %H:%M:%S")
        print(f"- Warehouse 2 (in stock for {delta.days} days)")
    
        
    
    order = input ("Do you want to place an order? (Y/N)")
    if order == "Y":
        order_number = int(input ("How much do you want to order?"))
        if order_number < number:
            print ("The order of", order_number, "Pieces of", item_name, "is placed")
        elif order_number > number or order_number == number:
            max_order = (input("We have that number or your order is even exceeding our storage. Do you want to place an order for maximum available? (Y/N)"))
            if max_order == "Y":
                print("The maximum amount of", item_name, "has been ordered!")

def search_category():
    os.system("clear")
    categories = {1:"Keyboard",2:"Smartphone",3:"Mouse",4:"Laptop",5:"Headphones",6:"Monitor",7:"Router",8:"Tablet"}
    temp = []
    for i in stock:
        counter1 = 0
        for b in categories:
            counter1 += 1
            if i["category"] in categories[counter1]:
                temp.append(counter1)           
    counter = 1
    for i in categories:
        print(f"{i}. {categories[i]} ({temp.count(counter)})")
        counter += 1
    menu_category = int(input("Type the number of the category to browse or press 42 to quit: "))
    if menu_category in range(1,9):
        for i in stock:
            if categories[int(menu_category)] == i["category"]:
                print(i["state"], i["category"],", Warehouse", i["warehouse"])
    elif menu_category == "42":
        pass       

menu()