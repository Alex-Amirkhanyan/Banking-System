import sys
import time
from connect_to_database import my_cursor, my_db


class ShowBalance:
    def __init__(self, money_amount, loan_arg, card_number, account_number):
        self._wrong_tries = 0
        self._loan = loan_arg
        self._card_number = card_number
        self._account_number = account_number
        self._money_amount = money_amount
        self._show_balance()

    def _show_balance(self):
        if self._validate_card_account_numbers():
            self._wrong_tries = 0
            print(f'\nYour balance is: {self._money_amount}$\n')
            if self._loan > 0:
                print(f'And your loan amount is: {self._loan}$')
            print('Restart the program to continue using it.')
        else:
            self._wrong_tries += 1
            if self._wrong_tries == 4:
                print('Limit of wrong inputs have achieved, try later.')
                sys.exit()
            print(f'Wrong card or account number, try again. Attempts left: {10 - self._wrong_tries}.')
            self._show_balance()

    def _validate_card_account_numbers(self) -> bool:
        inp = input('\nWrite your card or account number here (all together): ')
        if inp.isdigit():
            if len(inp) == 14:
                return int(inp) == int(self._account_number)
            elif len(inp) == 16:
                return int(inp) == int(self._card_number)
            return False
        else:
            print('You need to write only numbers.\n')
            return False


class WithdrawMoney:
    def __init__(self, email_arg, password_arg, money_amount_arg, card_number_arg, account_number_arg):
        self._wrong_tries = 0
        self._email = email_arg
        self.__password = password_arg
        self._money_amount = money_amount_arg
        self._card_number = card_number_arg
        self._account_number = account_number_arg
        self._withdraw_money_availability()

    def _withdraw_money_availability(self):
        if self._validate_card_account_numbers():
            if self._money_amount == 0:
                self._wrong_tries = 0
                print('Your balance is 0, you can\'t withdraw any amount of money.')
            else:
                self._wrong_tries = 0
                self._validate_withdrawing()
        else:
            self._wrong_tries += 1
            if self._wrong_tries == 4:
                print('Limit of wrong inputs have achieved, try later.')
                sys.exit()
            print(f'Wrong card or account number, try again. Attempts left: {10 - self._wrong_tries}.')
            self._withdraw_money_availability()

    def _validate_card_account_numbers(self) -> bool:
        inp = input('Write your card or account number here (all together): ')
        if len(inp) == 14:
            return int(inp) == int(self._account_number)
        elif len(inp) == 16:
            return int(inp) == int(self._card_number)
        return False

    def _validate_withdrawing(self):
        inp = input(f'Please write how much you would like to withdraw (available : {self._money_amount}): ')
        if inp.isdigit():
            if int(inp) > self._money_amount:
                self._wrong_tries += 1
                if self._wrong_tries == 4:
                    print('Limit of wrong inputs have achieved, try later.')
                    sys.exit()
                print('\nThe amount of money you want to withdraw can\'t exceed the amount of money '
                      'you have in your bank account.\n')
                self._validate_withdrawing()
            else:
                self._withdrawing_money(int(inp))
        else:
            self._wrong_tries += 1
            if self._wrong_tries == 4:
                print('Limit of wrong inputs have achieved, try later.')
                sys.exit()
            print('You need to write only numbers, nothing else. Try again.')
            self._validate_withdrawing()

    def _withdrawing_money(self, withdrawable_amount):
        time.sleep(1)
        print('\nProcessioning your request...')
        time.sleep(2.9)
        print('You can take your money. ')
        time.sleep(1.5)
        print(f'Your current balance is : {self._money_amount - withdrawable_amount}$')
        self._update_money_sql(withdrawable_amount)

    def _update_money_sql(self, withdrawable_amount):
        sql_command = "UPDATE client_list SET money_amount = %s WHERE email = %s and password = %s"
        values = (self._money_amount - withdrawable_amount, self._email, self.__password)
        my_cursor.execute(sql_command, values)
        print('\nRestart the program to continue using it.')


class DepositMoney:
    def __init__(self, email_arg, surname_arg, money_amount_arg):
        self._email = email_arg
        self.__password = surname_arg
        self._money_amount = money_amount_arg
        self._wrong_tries = 0
        self._insert_money()

    def _insert_money(self):
        inp = input('\nWrite the amount of money you want to deposit (as if you insert money for real) all together: ')
        if inp.isdigit():
            if len(inp) > 9:
                self._wrong_tries += 1
                if self._wrong_tries == 4:
                    print('Limit of wrong inputs have achieved, try later.')
                    sys.exit()
                print('You can\'t enter more than 9 characters, try again.')
                self._insert_money()
            else:
                self._add_money_to_account(int(inp))
        else:
            self._wrong_tries += 1
            if self._wrong_tries == 4:
                print('Limit of wrong inputs have achieved, try later.')
                sys.exit()
            print('You need to write only numbers, nothing else. Try again.')
            self._insert_money()

    def _add_money_to_account(self, inp_arg):
        sql_command = f"UPDATE client_list SET money_amount = %s WHERE email = %s AND password = %s"
        values = (self._money_amount + inp_arg, self._email, self.__password)
        my_cursor.execute(sql_command, values)
        my_db.commit()
        print(f'\nThe money have been added to your account, your current balance is: {self._money_amount + inp_arg}$')
        print('Restart the program to continue using it.')
