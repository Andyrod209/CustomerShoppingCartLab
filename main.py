from product import Products
from shopping_cart import ShoppingCart

view_product = Products()
view_product.price_of_product()
view_product.category()


cart = ShoppingCart()
cart.add_product()
cart.number_of_products()