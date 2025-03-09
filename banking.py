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

    

    
    







  
