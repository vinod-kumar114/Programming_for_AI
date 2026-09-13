# the concept of combining data and methods inside a class while controlling access to the internal data. Private variables and methods such as getters and setters can be used to protect data from inappropriate modification.

#  Here we use methods getter and setter to protect data and get the work done.


# ===== Getter and Setter =====
# A getter is a method used to retrieve the value of a private variable, while a setter is used to modify its value. Setters can also be used to validate data before changing it.



class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance=balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

    def set_balance(self,balance):
        self.__balance=balance



account = BankAccount("Ali", 5000)
account.deposit(2000)
account.withdraw(1000)
print("Balance:", account.get_balance())

account.set_balance(15000)
print("The new balance is:", account.get_balance())
