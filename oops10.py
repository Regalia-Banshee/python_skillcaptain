class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def display_info(self):
        print(f"{self.name},{self.price},{self.quantity}")
class Cart:
    def __init__(self,cust_name):
        self.cust_name=cust_name
        self.cart_content=[]
    def add_to_cart(self,product):
        self.cart_content.append(product)


    def remove_from_cart(self,product_name):
        for product in self.cart_content:
            if product_name==product.name:
                self.cart_content.remove(product)

            else:
                print("Product not found")

    def display_cart(self):
        if self.cart_content:
            for product in self.cart_content:
                product.display_info()
        else:
            print("Cart is empty")
product1=Product('chips',10,2)
product2=Product('chocolates',2,10)

def Cart_display():
    product1 = Product('chips', 10, 2)
    product2 = Product('chocolates', 2, 10)
    cart=Cart('Sushmita')
    cart.add_to_cart(product2)
    cart.add_to_cart(product1)
    cart.display_cart()

    cart.remove_from_cart('chocolates')
    cart.remove_from_cart('chips')
    cart.display_cart()



Cart_display()