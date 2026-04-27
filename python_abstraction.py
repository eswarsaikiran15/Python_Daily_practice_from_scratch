from abc import ABC, abstractmethod
#abstract class
class Atm(ABC):
    @abstractmethod
    def withdraw(self,amount):
        pass #why pass : Python requires every block (function, class, loop, condition) to have at least one statement.When you don’t want to write logic yet, you use pass as a placeholder.
    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def check_balance(self):
        pass
# concrete class
class Sbi_atm(Atm):
    def __init__(self,balance):
        self.balance = balance
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"withdrawn:{amount},remaining balance: {self.balance}")
        else:
            print("insufficient balance")
    def deposit(self,amount):
        self.balance += amount
        print(f"deposited:{amount},remaining balance: {self.balance}")
    def check_balance(self):
        print(f"checking balance: {self.balance}")

#using abstraction
# ---- Using the ATM ----

# Creating an object of SBI ATM with initial balance
user_1 = Sbi_atm(10000)

# Performing operations
user_1.withdraw(100)     # deducts 100
user_1.deposit(1100)     # adds 1100
user_1.check_balance()   # shows final balance