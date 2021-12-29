class Products:

    def __init__(self):
        self.product_name = input("product name? ")
        print(self.product_name)
        
    def price_of_product(self):
        self.price = input("how much is it? ")
        print('price of', self.product_name,'is', self.price)
    
    def category(self):
        # variables are category but cat short
        self.cat = input("what category is it part of? ")
        print(self.cat) 