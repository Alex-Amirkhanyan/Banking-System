import sys
import time
import getpass
import hashlib
from connect_to_database import my_cursor, my_db


class GetLoan:
    def __init__(self, money_amount_arg, loan_amount_arg, email_arg, password_arg):
        self._wrong_tries = 0
        self._money_amount = money_amount_arg
        self._loan = loan_amount_arg
        self._email = email_arg
        self.__password = password_arg
        self.compare_passwords()

    def compare_passwords(self):
        inp = getpass.getpass('Please write your password again to continue: ')
        if hashlib.sha224(inp.encode()).hexdigest() == self.__password:
            self.check_loan_existence()
        else:
            self._wrong_tries += 1
            if self._wrong_tries == 4:
                print('Limit of wrong inputs have achieved, try later.')
                sys.exit()
            print('Wrong password try again.\n')
            self.compare_passwords()

    def check_loan_existence(self):
        if self._loan > 0:
            print('\nYou already have loan that you need to pay, you can\'t get more.')
            print('Restart the program to continue using it.')
        else:
            self.show_possible_loan_amount()

    def show_possible_loan_amount(self):
        if self._money_amount == 0:
            print('The max. amount of loan you can get is: 10000$')
            self.ask_if_wants_loan(10000)
        else:
            print(f'The max. amount of loan you can get is: {self._money_amount * 5}$')
            self.ask_if_wants_loan(self._money_amount * 5)

    def ask_if_wants_loan(self, max_amount_arg):
        inp = input('\nWhat is the amount of loan you would like to get? If you don\'t want loan type 0: ')
        self.loan_request_validator(inp, max_amount_arg)

    def loan_request_validator(self, inp_arg, max_amount_arg):
        if inp_arg.isdigit():
            if int(inp_arg) == 0:
                print('Very well, restart the program to continue using it.')
                sys.exit()
            if int(inp_arg) > max_amount_arg:
                self._wrong_tries += 1
                if self._wrong_tries == 4:
                    print('Limit of wrong inputs have achieved, try later.')
                    sys.exit()
                print('\nThe amount of money you want to get can\'t exceed the max. amount you can get. Try again.\n')
                self.ask_if_wants_loan(max_amount_arg)
            else:
                self._wrong_tries = 0
                self.give_the_loan(int(inp_arg))
        else:
            self._wrong_tries += 1
            if self._wrong_tries == 4:
                print('Limit of wrong inputs have achieved, try later.')
                sys.exit()
            print('You need to write only numbers, nothing else. Try again.')
            self.ask_if_wants_loan(max_amount_arg)

    def give_the_loan(self, loan_amount_arg):
        sql_command = "UPDATE client_list SET money_amount = %s, loan_amount = %s WHERE email = %s AND password = %s"
        values = (self._money_amount+loan_amount_arg, loan_amount_arg, self._email, self.__password)
        my_cursor.execute(sql_command, values)
        my_db.commit()
        print('\nFetching your request...')
        time.sleep(3)
        print('\nLoan has been successfully given, check your account to see it.')
        print('Restart the program to continue using it.')


class PayLoan:
    def __init__(self, money_amount_arg, loan_amount_arg, email_arg, password_arg):
        self._wrong_tries = 0
        self._money_amount = money_amount_arg
        self._loan = loan_amount_arg
        self._email = email_arg
        self.__password = password_arg
        self.compare_passwords()

    def compare_passwords(self):
        inp = getpass.getpass('Please write your password here: ')
        if hashlib.sha224(inp.encode()).hexdigest() == self.__password:
            self.ask_payment_amount()
        else:
            self._wrong_tries += 1
            if self._wrong_tries == 4:
                print('Limit of wrong inputs have achieved, try later.')
                sys.exit()
            print('Wrong password try again.\n')
            self.compare_passwords()

    def ask_payment_amount(self):
        inp = input(f'\nYour current loan is {self._loan}$, write here how much you would like to pay: ')
        if inp.isdigit():
            self.validate_payment_amount(int(inp))
        else:
            self._wrong_tries += 1
            if self._wrong_tries == 4:
                print('Limit of wrong inputs have achieved, try later.')
                sys.exit()
            print('You need to write only numbers, nothing else. Try again.')
            self.ask_payment_amount()

    def validate_payment_amount(self, inp_arg):
        if inp_arg > self._loan:
            print('\nThe additional amount of money will be added to your bank account.')
            self.loan_payment(inp_arg, inp_arg-self._loan)
        else:
            self.loan_payment(inp_arg, 0)

    def loan_payment(self, inp_arg, additional_amount_arg):
        if additional_amount_arg > 0:
            sql_command = "UPDATE client_list SET money_amount = %s, loan_amount = %s WHERE email = %s AND password = %s"
            values = (self._money_amount+additional_amount_arg, 0, self._email, self.__password)
        else:
            sql_command = "UPDATE client_list SET loan_amount = %s WHERE email = %s AND password = %s"
            values = (self._loan-inp_arg, self._email, self.__password)
        my_cursor.execute(sql_command, values)
        my_db.commit()
        time.sleep(2)
        print('\nFetching your request...')
        time.sleep(3)
        print('Payment went successfully. Restart the program to continue using it.')
