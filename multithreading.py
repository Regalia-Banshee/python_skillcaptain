from threading import *

class Rolling_dough(Thread):
    def run(self):
        print(f"We are rolling the dough")

class Chopping_Veggies(Thread):
    def run(self):
        print(f"We are chopping veggies")

class Making_pizza(Thread):
    def run(self):
        print(f"We are making pizza")

object1=Rolling_dough()
object2=Chopping_Veggies()
object3=Making_pizza()

object1.start()
object2.start()
object3.start()

object1.join()
object2.join()
object3.join()

print(f"Tasty pizza is ready")