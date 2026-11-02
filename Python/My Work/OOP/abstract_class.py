from abc import ABC, abstractmethod

class Account(ABC):

    @abstractmethod
    def calculate_interest(self):  # it is creating an abstract function, tht will be used by all the sub-classes
        pass

class SavingsAccount(Account):

    def calculate_interest(self): # abstract method used in child class
        print("Interest is 5%")

s1 = SavingsAccount()

s1.calculate_interest()
    