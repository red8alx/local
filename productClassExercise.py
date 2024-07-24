#Exercise 2: Creating a Product Catalog
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calc_value(self):
        total_value = self.price * self.quantity
        print(f"The total value of \'{self.name}\' in stock is: {total_value}")
my_product = Product("Table Salt", 100, 2)
my_product.calc_value()
        