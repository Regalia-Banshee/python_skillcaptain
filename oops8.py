class User:
    def __init__(self,user_name,email,password):
        self.user_name=user_name
        self.email=email
        self.password=password

    def display_info(self):
        print(f"Users Name is: {self.user_name}")
        print(f"Email adress is : {self.email}")
        print(f"Password is: {self.password}")

data_base = []
def registration():
    print("Welcome to user registration")
    user_name=input("Enter user name: ")
    email=input("Enter email: ")
    print("Email verified")
    for user in data_base:
        if user.email==email:
            print("Email already in use")
            return



    password=input("Enter password: ")


    first_user=User(user_name,email,password)
    data_base.append(first_user)
    first_user.display_info()


while True:
    registration()
    next_user=input("Do you want to register new user?(y/n)?: ")
    if next_user!="y":
        break

