import csv


class Account:
    def init(self, account_id, first_name, last_name, password, balance=0 ):
       self.account_id=account_id
       self.first_name=first_name
       self.last_name=last_name
       self.password=password
       self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > 0 and self.balance - amount >= -100:
            if self.balance < 0 and amount > 100:
                print("Transaction denied: Cannot withdraw more than $100 when account is negative.")
                return
            self.balance -= amount
            if self.balance < 0:
             print(f"Withdrew ${amount}. New Balance: ${self.balance}")
        else:
            print(f"Withdraw failed! Current balance: ${self.balance}, cannot withdraw ${amount}.")

    def get_balance(self):
        return self.balance
    
    
    

class CheckingAccount(Account):
    def __init__(self, account_id, first_name, last_name, password, balance=0):
        super().__init__(account_id, first_name, last_name, password, balance)

class SavingAccount(Account):
    def __init__(self, account_id, first_name, last_name, password, balance=0):
        super().__init__(account_id, first_name, last_name, password, balance)
