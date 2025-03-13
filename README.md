# Python Banking Project

## Project Description 
This is a **Python Banking Project** developed in Python. The system allows customers to create their own bank accounts with checking and savings options. Customers can deposit and withdraw money, transfer funds between their accounts, and even transfer money to other customers. The system manages overdrafts by charging fees and deactivating accounts after excessive overdrafts. Data is stored persistently using CSV files. 


## Technologies Used 
1- Python 3

2- CSV file handling for data storage 

3- Object-Oriented Programming (OOP) for system design 

4- Console-based User Interface for interaction  

## App Functionality 
| Feature                                    | Description                                         |
|--------------------------------------------|-----------------------------------------------------|
| **Add Customer**                           | Create a new customer with checking and savings accounts |
| **Login**                                  | Login using customer ID and password                |
| **Withdraw**                               | Withdraw funds (limit $100 per transaction, $35 overdraft fee) |
| **Deposit**                                | Deposit funds into checking or savings account    |
| **Transfer between own accounts**          | Transfer funds between checking and savings accounts |
| **Transfer to other customer**             | Send money to another customer's account          |
| **Account Info**                           | Display customer’s account balances and overdraft counts |
| **Account Deactivation/Overdraft**         | Account deactivates after 2 overdrafts, can be reactivated by deposit |

## Challenges & Key Takeaways 

## Challenges: 
- Handling **overdraft scenarios** and **account deactivation/reactivation** properly. 

- Maintaining accurate **data persistence using CSV** files while supporting multiple customers. 

-Creating a **secure login** and validating user input effectively. 

-Designing an **intuitive command-line menu system** for users to interact with. 

## Key Takeaways: 
Learned how to design and implement **OOP systems in Python** effectively. 
Gained experience in **file handling and data persistence**. 
Improved understanding of **error handling and validation**. 
Practiced writing **modular and maintainable code**. 

## IceBox Features (Future Work) 
-Graphical User Interface (GUI) to improve user experience. 

-Admin dashboard to monitor all customer accounts and transactions.

-Transaction history logs for each customer. 

-Password reset and account recovery system. 

-Email notifications for transactions and account activities. 

-Interest calculation system for savings accounts. 

-Loan request and approval management.