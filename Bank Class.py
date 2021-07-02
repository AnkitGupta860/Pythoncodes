import sys
class Bank(object):
    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self,Amount):
        self.balance += Amount
        return self.balance

    def withdraw(self,Amount):
        if (Amount>self.balance):
            print("Not enough money")
        else:
            self.balance-=Amount
        return self.balance

name = input("Enter Name :")
b = Bank(name)
while True:
    print("d - Deposit, w - withdraw, e - Exit")
    choice = input("your choice: ")
    if choice=="e" or choice=="E":
        sys.exit

    amt = int(input("Enter Amount"))
    if choice=="d" or choice=="D":
        print("Balance after deposit: ",b.deposit(amt))
    elif choice=="w" or choice=="W":
        print("Balance After Withdraw: ",b.withdraw(amt))





