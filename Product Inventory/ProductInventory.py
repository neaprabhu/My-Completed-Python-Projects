'''
Project Name: Product Inventory Project

Project Description: Create an application which manages an inventory of products. Create a product class which has a price, id, and quantity on hand. Then create an inventory class which keeps track of various products and can sum up the inventory value.

Author: Navin Prabhu

Date: 2020 Quarantine
'''

class Product():
    def __init__(self, price, id, quantity):
        self.price = price
        self.id = id
        self.quantity = quantity

    def __str__(self):
         decomp = 'Product ID = ' + self.id + '\n'
         decomp = decomp + 'Price = ' + self.price + '\n'
         decomp = decomp + 'Quantity = ' + self.quantity + '\n'
         return decomp


class Inventory():
    def __init__(self, maxproducts = 5):
        self.maxproducts = maxproducts
        self.myinventory = []
        self.inventoryvalue = 0

    def addproduct(self, myproduct):
        self.myinventory.append(myproduct)
        self.inventoryvalue += (myproduct.quantity)*(myproduct.price)

    def listinventory(self):
        print('Current Inventory Breakdown:')
        print('----------------------------------')
        print('Product ID\tProduct Price\tProduct Quantity\tTotal Value')
        for i in self.myinventory:
            print(i.id, i.price, i.quantity, i.price*i.quantity, sep='\t')
        print('Total Inventory Value = {}'.format(self.inventoryvalue))

    def removeproduct(self, product):
        self.inventoryvalue -= product.price * product.quantity
        self.myinventory.remove(product)

product_id = ('TV', 'Phone', 'Radio', 'Laptop')
product_price = (300, 800, 100, 500)
product_quantity = (10, 50, 5, 25)

myinventory = Inventory()
for i in range(0,len(product_id)):
    myinventory.addproduct(Product(product_price[i], product_id[i], product_quantity[i]))

myinventory.listinventory()
myinventory.removeproduct(myinventory.myinventory[0])
myinventory.listinventory()




