
class ShoppingCart:
    def __init__(self):
        self.products_list = []
        print(self.products_list)
    
    def number_of_products(self):
        self.len_of_list = len(self.products_list)
        print("you have", self.len_of_list, 'item in your cart.')

    def add_product(self):
        new_product = input('What product would you like to add? ')
        self.products_list.append(new_product) 