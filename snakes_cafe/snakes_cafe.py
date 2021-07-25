print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears


""")

menu=[
    "Wings",
"Cookies",
"Spring Rolls",
"Salmon",
"Steak",
"Meat Tornado",
"A Literal Garden",
"Ice Cream",
"Cake",
"Pie",
"Coffee",
"Tea",
"Unicorn Tears",
    ]

num=[0,0,0,0,0,0,0,0,0,0,0,0,0]

order=input("What would you like to order? ",)



def order_food(order):
    while order !="quit":
        if order in menu:
            num[menu.index(order)]+=1
            print(f"{num[menu.index(order)]} order of {order} have been added to your meal ")
        else:
            print("not in the menu")
            
        order=input("What would you like to order? ")

order_food(order)

for i in range(13):
    if num[i]!=0:
        print(f"{num[i]} order of {menu[i]}  have been added to your meal")


