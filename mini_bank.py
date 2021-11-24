class customer:
    "this class developed by vaibhav and describes bank operatinos"
    bank_name='SBI'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("*"*30)
        print("you are depositing {} amount".format(amount))
        print("balance after deposit",self.balance)
        print("*"*30)
    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficiant balance")
        else:
            self.balance=self.balance-amount
            print("*"*30)
            print("you are withdrawing {} amount".format(amount))
            print("balance after withdrawing",self.balance)
            print("*"*30)
    def info(self):
        print("*"*30)
        print("welcome to {} bank".format(customer.bank_name))
        print("customer name",self.name,"balance is", self.balance)
        print("*"*30)

print("welcome to {} bank".format(customer.bank_name))
name=input("enter the name of customer")
c=customer(name)
while True:
    print("welcome {}, your account is created and you balance is {} ".format(name,c.balance))
    print(" d-deposit\nw-withdraw\ni-info of your account\ne-exit")
    option=input("enter you option:- ")
    if option.lower() == 'd' :
        amount=float(input("how much amount you want to deposit"))
        c.deposit(amount)
    elif option.lower() == 'w':
        amount=float(input("enter amount you want to withdraw"))
        c.withdraw(amount)
    elif option.lower() == 'i':
        c.info()
    elif option.lower() == 'e':
        print("*"*30)
        print("thanks for banking with us")
        print("*"*30)
        break
    else:
        print("*"*30)
        print("please enter correct option")
        print("*"*30)
        



    