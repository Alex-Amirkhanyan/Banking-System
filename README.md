# Basic Banking System

The following project is a basic banking system written in Python and MySql. To run it, you need to download [MySql](https://www.mysql.com/downloads/) to be able to run the program with no problems and [MySql Workbench](https://dev.mysql.com/downloads/workbench/) to see users' data. After downloading these programs, you can proceed to download the code. To run the program successfully, open the command prompt (CMD) and execute the "main.py" file.
```bash
python "the path of the folder here"\main.py
```

## About files

`connect_to_database.py`: This file establishes the connection to the database. To ensure seamless execution, please modify the connection settings in the code according to your database configuration. Additionally, within the commented lines of code, there is a provision to add sample users to the database. Feel free to include your own user data for testing purposes.

`main.py`: This is the main file of the project, responsible for initiating the execution of the code. When running this file, you will be presented with two options: Login and Sign up. Depending on your selection, the corresponding class will be invoked to handle the chosen operation.
 
`login.py`: This file is responsible for handling the login functionality of the banking system. Upon successful login, it calls the `post_login_operations.py` file.

`post_login_operations.py`: This file provides a menu of actions that can be performed after logging in. These actions include:

- Show balance (Action is in the `money_operations.py` file)
- Change account details (Action is in the `connect_to_database.py` file)
- Withdraw money (Action is in the `money_operations.py` file)
- Deposit money (Action is in the `money_operations.py` file)
- Get a loan (Action is in the `loan_operations.py` file)
- Pay a loan (Action is in the `loan_operations.py` file)

All the necessary classes for these actions are imported in this file. Once you choose an action, the corresponding class is invoked to execute the desired operation. Any changes made during the process are then updated in the database.

And finally `sign_up.py`: This file handles the registration process for the banking system. Upon correctly entering all the required information, it generates unique card and account numbers for future use. Additionally, it adds all the provided data to the database for record-keeping.
