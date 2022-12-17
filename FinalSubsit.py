class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ': $' + str(self.price)

    def getprice(self, count):
        totalprice = self.price * count
        
        #Round 
        return round(totalprice)
    
menuitem1 = MenuItem('Chicken', 6.99)
menuitem2 = MenuItem('Beef', 8.99)
menuitem3 = MenuItem('Potatoes', 3.99)
menuitem4 = MenuItem('Carrots', 2.99)
menuitem5 = MenuItem('Green Beans', 2.99)

menuitems = [menuitem1, menuitem2, menuitem3, menuitem4, menuitem5]

index = 0

for menu_item in menuitems:
    print(str(index) + '. ' + menu_item.info())
    index += 1

print('--------------------')

order = int(input('Enter menu item number: '))
selected_menu = menuitems[order]
print('Selected item: ' + selected_menu.name)

count=int(input('Enter quantity: '))

result=selected_menu.getprice(count)

#Output
print('Your total is $'+str(result))