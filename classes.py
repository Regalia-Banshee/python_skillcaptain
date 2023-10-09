class BankAccount:
    def __init__(self, ac_no, ac_holder, ac_balance):
        self.ac_no = ac_no
        self.ac_holder = ac_holder
        self.ac_balance = ac_balance

    def deposit(self):
        depo=int(input("Enter amount to deposit: "))
        self.ac_balance += depo
        bal=input("Do you want to display your balance(y/n): ")
        if bal=="y":
            print(f"Your balance is: {self.ac_balance}")
        elif bal=="n":
            print("Have a nice day")
        else:
            print("Enter either y/n")



    def withdraw(self):
        withd = int(input("Enter amount to withdraw: "))
        if self.ac_balance <= withd:
            print(f"Insufficient Balance")
        else:
            self.ac_balance -= withd
        bal = input("Do you want to display your balance(y/n): ")
        if bal == "y":
            print(f"Your balance is: {self.ac_balance}")
        elif bal =="n":
            print("Have a nice day")
        else:
            print("Enter either y/n")

    def display_info(self):
        print(f"Account no: {self.ac_no}")
        print(f"Account Balance: {self.ac_balance}")
        print(f"Account Holder: {self.ac_holder}")
