import csv

class Account:
    def __init__(self, balance=0):
        self.balance = int(balance)
        self.overdraft_count = 0
        self.deactivated = False
        
    def deposit(self, amount):
        if self.deactivated and self.balance + amount > 0:
            self.deactivated = False
            self.overdraft_count = 0
            print("Account reactivated after deposit.")
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
        
    def withdraw(self, amount):
        if self.deactivated:
            print("Account is deactivated due to overdraft.")
            return False
        if amount > 100:
            print("Cannot withdraw more than $100 in one transaction.")
            return False
        if self.balance - amount < 0:
            self.overdraft_count += 1
            self.balance -= 35
            print(f"Overdraft! Charged $35. Balance is now ${self.balance}")
            if self.overdraft_count > 2:
                self.deactivated = True
                print("Account deactivated due to excessive overdrafts.")
            return False
        self.balance -= amount
        print(f"Withdrawn ${amount}. New balance: ${self.balance}")
        return True
    
    def transfer_between_accounts(self, target_account, amount):
        if self.withdraw(amount):
            target_account.deposit(amount)
            print(f"Transferred ${amount} between your own accounts successfully \U0001F44D.")
            
    def transfer_to_other_customer(self, recipient_account, amount):
        if self.withdraw(amount):
            recipient_account.deposit(amount)
            print(f"Transferred ${amount} to another customer successfully \U0001F44D.")

class Customer:
    
    def __init__(self, customer_id, first_name, last_name, password, checking_balance=0, savings_balance=0):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.checking = Account(checking_balance)
        self.savings = Account(savings_balance)
        
    def show_info(self):
        print(f"\n--- Account Information for {self.first_name} {self.last_name} ---")
        print(f"Customer ID: {self.customer_id}")
        print(f"Checking Balance: ${self.checking.balance}")
        print(f"Savings Balance: ${self.savings.balance}")
        print(f"Checking Overdrafts: {self.checking.overdraft_count}")
        print(f"Savings Overdrafts: {self.savings.overdraft_count}")
        
    def to_list(self):
        return [
            self.customer_id,
            self.first_name,
            self.last_name,
            self.password,
            self.checking.balance,
            self.savings.balance
        ]

class Bank:
    
    def __init__(self, filename="bank.csv"):
        self.filename = filename
        self.customers = self.load_customers()
        
    def load_customers(self):
        customers = {}
        try:
            with open(self.filename, "r") as file:
                reader = csv.reader(file, delimiter=';')
                next(reader)
                for row in reader:
                    customers[row[0]] = Customer(row[0], row[1], row[2], row[3], int(row[4]), int(row[5]))
        except FileNotFoundError:
            print("No existing bank records found.")
        return customers
    
    def save_customers(self):
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(["customer_id", "first_name", "last_name", "password", "checking_balance", "savings_balance"])
            for customer in self.customers.values():
                writer.writerow(customer.to_list())
                
    def add_customer(self):
        customer_id = input("Enter customer ID: ")
        if customer_id in self.customers:
            print("Customer ID already exists.")
            return
        first_name = input("First name: ")
        last_name = input("Last name: ")
        password = input("Password: ")
        checking_balance = int(input("Checking balance: "))
        savings_balance = int(input("Savings balance: "))
        self.customers[customer_id] = Customer(customer_id, first_name, last_name, password, checking_balance, savings_balance)
        self.save_customers()
        print("Customer added successfully \U0001F44D.")
        
    def get_customer(self, customer_id):
        return self.customers.get(customer_id)
    
    def verify_password(self, customer, password):
        return customer.password == password

class BankSystem(Bank):
    
    def __init__(self):
        super().__init__()
        
    def main_menu(self):
        while True:
            print("\n *** \U0001F3E6 Welcome to the Bank \U0001F3E6 *** ")
            print("1. Add Customer")
            print("2. Login")
            print("3. Exit")
            choice = input("Please Choose one of the following option: ")
            if choice == "1":
                self.add_customer()
            elif choice == "2":
                self.login()
            elif choice == "3":
                self.save_customers()
                print("Exiting. Goodbye \U0001F44B")
                break
            else:
                print("Invalid choice \u274C.")
                
    def login(self):
        customer_id = input("Please enter Customer ID: ")
        customer = self.get_customer(customer_id)
        if customer:
            password = input("Please enter Password: ")
            if self.verify_password(customer, password):
                print(f"\n welcome, dear customer\U0001F44B, \u2B50 {customer.first_name} {customer.last_name} \u2B50")
                self.customer_menu(customer)
            else:
                print("Incorrect password \u274C.")
        else:
            print("Customer not found.")
            
    def customer_menu(self, customer):
        while True:
            print("\n----- Account Menu -----")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Transfer between own accounts")
            print("4. Transfer to another customer")
            print("5. Show account info")
            print("6. Logout")
            choice = input("Please Choose one of the following option: ")
            if choice == "1":
                acc = input("From (checking | savings): ")
                amount = int(input("Amount: "))
                account = customer.checking if acc == "checking" else customer.savings
                account.withdraw(amount)
                self.save_customers()
            elif choice == "2":
                acc = input("To (checking | savings): ")
                amount = int(input("Amount: "))
                account = customer.checking if acc == "checking" else customer.savings
                account.deposit(amount)
                self.save_customers()
            elif choice == "3":
                from_acc = input("From (checking | savings): ")
                to_acc = input("To (checking | savings): ")
                amount = int(input("Amount: "))
                from_account = customer.checking if from_acc == "checking" else customer.savings
                to_account = customer.checking if to_acc == "checking" else customer.savings
                from_account.transfer_between_accounts(to_account, amount)
                self.save_customers()
            elif choice == "4":
                recipient_id = input("Please enter the customer ID to transfer to: ")
                recipient = self.get_customer(recipient_id)
                if recipient:
                    from_acc = input("From (checking | savings): ")
                    to_acc = input("To (checking | savings): ")
                    amount = int(input("Amount: "))
                    from_account = customer.checking if from_acc == "checking" else customer.savings
                    recipient_account = recipient.checking if to_acc == "checking" else recipient.savings
                    from_account.transfer_to_other_customer(recipient_account, amount)
                    self.save_customers()
                else:
                    print("Customer not found.")
            elif choice == "5":
                customer.show_info()
            elif choice == "6":
                print("Logging out...")
                break
            else:
                print("Invalid option.")
                
if __name__ == "__main__":
    bank_system=BankSystem()
    bank_system.main_menu()