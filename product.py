class Products:

    def __init__(self, product_name):
        self.product_name = product_name
        print(product_name)

    def price(self):
        products_price = input("what is the price of this product? ")
        print('product price is', products_price)
    
    def category(self):
        item_cat = input('What category is this item? ')
        print('product is a', item_cat)
        