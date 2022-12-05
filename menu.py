###The menu should display items available for order according to the inventory, and be called
###by the order class


###Get Inventory --- have to pull from inventory to find out what is and isn't available


###Menu class is initiated 
class menu:
    def __init__(self,item,price):
        self.item = item
        self.price = price
        


def menudisplay(items,prices):
    itemmenu=[]
    for i in range(len(items)):
        itemmenu.append(menu(items[i], prices[i]))
    return itemmenu


# Menu Items 
items = ['Chicken', 'Beef', 'Lamb', 'Carrots', 'Green Beans', 'Brocoli', 'Potatoes', 'Squash']

# prices
prices = [1,2,3,4,5,6,7,8]

# Menu Listing
Foods = menudisplay(items, prices)

x = 1
for any in Foods:
    print(x,'. ', any)
    x = x + 1