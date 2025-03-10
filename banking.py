import csv

BankFile = "bank.csv"

class Account:
    def __init__(self, balance_checking=0.0, balance_savings=0.0):
        self.balance_checking = balance_checking
        self.balance_savings = balance_savings

    def deposit(self, amount, account_type="checking"):
        if amount > 0:
            if account_type == "checking":
                self.balance_checking += amount
            else:
                self.balance_savings += amount
            print(f"${amount} deposited into {account_type} account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount, account_type="checking"):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if account_type == "checking":
            if amount > self.balance_checking:
                print("Insufficient funds in checking account.")
            elif self.balance_checking - amount < -100:
                print("Cannot withdraw, balance cannot be less than -$100.")
            else:
                self.balance_checking -= amount
                print(f"${amount} withdrawn from checking account.")
        else:
            if amount > self.balance_savings:
                print("Insufficient funds in savings account.")
            else:
                self.balance_savings -= amount
                print(f"${amount} withdrawn from savings account.")

class Customer:
    def __init__(self, account_id, first_name, last_name, password, balance_checking=0.0, balance_savings=0.0):
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.account = Account(balance_checking, balance_savings)

class Bank:
    def __init__(self):
        self.customers = self.customer_data() 