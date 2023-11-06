class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def print_product_info(self):
        print(f"{self.name},{self.price},{self.quantity}")


def product_registration():
    cart=[]
    run=1
    while run==True:
        try:
            name = input("Enter product name: ")
            price=float(input("Enter product price: "))
            quantity=int(input("Enter Quantity: "))
            user = Product(name, price, quantity)
            cart.append(user)
            user.print_product_info()
            run=False
        except ValueError:
            print("Enter numbers")


product_registration()


