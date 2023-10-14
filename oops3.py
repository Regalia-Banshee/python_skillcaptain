class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def vehicle_brand(self):
        print(f"This vehicle is made by {self.brand}")

    def vehicle_model(self):
        print(f"This is the {self.brand}{self.model} ")

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")




parent_class = Vehicle(input("Enter vehicle brand: "),input("enter model: "))
parent_class.display_info()

class Truck(Vehicle):
    def __init__(self,brand,model,load_capacity):
        super().__init__(brand, model)
        self.load_capacity=load_capacity


    def display_info(self):
        super().display_info()
        print(f"Load capacity: {self.load_capacity}kg")
run=1
while run==True:
    try:
        child_class=Truck(input("Enter vehicle brand: "),input("enter model: "),int(input("Enter  load capacity: ")))
        child_class.display_info()
        run=False

    except ValueError:
        print("Enter numbers!!!!")

