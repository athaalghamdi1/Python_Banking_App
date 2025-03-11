import csv

BankFile = "bank.csv"

class Account:
    def __init__(self, balance_checking=0, balance_savings=0):
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

    def transfer(self, amount, from_account="checking"):
        if amount <= 0:
            print("Transfer amount must be positive.")
            return

        if from_account == "checking":
            if amount > self.balance_checking:
                print("Insufficient funds in checking account.")
            else:
                self.balance_checking -= amount
                self.balance_savings += amount
                print(f"${amount} transferred from checking to savings.")
        else:
            if amount > self.balance_savings:
                print("Insufficient funds in savings account.")
            else:
                self.balance_savings -= amount
                self.balance_checking += amount
                print(f"${amount} transferred from savings to checking.")

class Customer(Account):
    def __init__(self, account_id, first_name, last_name, password, balance_checking=0, balance_savings=0):
        super().__init__(balance_checking, balance_savings) 
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        
class Bank:
    def __init__(self):
        self.customers = self.customer_data()

    def customer_data(self):
        customers = {}
        try:
            with open(BankFile, mode="r") as file:
                reader = csv.reader(file)
                next(reader)  
                for row in reader:
                    if len(row) == 6:
                        customers[row[0]] = Customer(row[0], row[1], row[2], row[3], float(row[4]), float(row[5]))
        except FileNotFoundError:
            print("Error: bank.csv file not found.")
        return customers 

    def save_customer(self, customer):
        customers_list = []
        try:
            with open(BankFile, mode="r") as file:
                reader = csv.reader(file)
                next(reader)  
                for row in reader:
                    if row[0] == customer.account_id:
                        row[4] = str(customer.balance_checking)
                        row[5] = str(customer.balance_savings)
                    customers_list.append(row)
        except FileNotFoundError:
            print("Error: bank.csv file not found.")