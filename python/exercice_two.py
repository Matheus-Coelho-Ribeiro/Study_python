#exercice 2 shopping cart program

name_item = input("enter the name of item\n")
item_price = float(input("\nenter the price of item\n"))
quantity_item = int(input("\nenter the quantity of item\n"))

money_totaly = item_price * quantity_item

print(f"the name item is {name_item}, your have {quantity_item} and price of one item is {item_price}, totaly of money is {money_totaly}")