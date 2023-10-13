class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def print_age(self):
        print(f"Hi, I am {self.age} years old")
    def print_name(self):
        print(f"Hi, I am {self.name}")

first_person=Person("Alice",25)
first_person.print_name()
first_person.print_age()


second_person=Person("Bob",30)
second_person.print_name()
second_person.print_age()
