class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, blc):
        if blc>0:
            self.__balance+=blc

    def withdraw(self, blc):
        if blc<=self.__balance:
            self.__balance-=blc
        else:
            print("Insufficient balances")


ba = BankAccount("Vinod", 500000)
print(ba.get_balance())

ba.deposit(2000)
print(ba.get_balance())

ba.withdraw(5000)
print(ba.get_balance())