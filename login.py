import sys
import hashlib
import getpass
from connect_to_database import my_cursor
from post_login_operations import PostLoginOperations


class InputLoginValidator:
    def __init__(self):
        self.wrong_login_inputs = 0
        self._login_inp = None
        self._password_inp = None
        self._login_inp_type = None
        self.show_login_lines()

    def show_login_lines(self):
        self._login_inp = input('\nWrite your phone number or email: ')
        self._password_inp = getpass.getpass('Write your password: ')
        if self.login_validator(self._login_inp) and self.password_validator(self._password_inp):
            self._login_inp_type = self.login_type(self._login_inp)
            self._find_in_sql()
        else:
            self.wrong_login_inputs += 1
            if self.wrong_login_inputs == 3:
                print('Maximum amount of tries has been achieved, try again later. ')
                sys.exit()
            else:
                print(f'User not found try again. Tries left: {3 - self.wrong_login_inputs}')
                self.show_login_lines()

    def _find_in_sql(self):
        sql_command = f"SELECT name, surname, age, email, phone_number, card_number, account_number, money_amount," \
                      f" loan_amount, password FROM client_list WHERE {self._login_inp_type} = '{self._login_inp}'" \
                      f" and password = '{hashlib.sha224(self._password_inp.encode()).hexdigest()}'"
        my_cursor.execute(sql_command)
        res = my_cursor.fetchall()
        self._sql_res_validator(res)

    def _sql_res_validator(self, res):
        if len(res) > 0:
            PostLoginOperations(res)
        else:
            self.wrong_login_inputs += 1
            if self.wrong_login_inputs == 3:
                print('Maximum amount of tries has been achieved, try again later. ')
                sys.exit()
            else:
                print(f'User not found try again. Attempts left: {3 - self.wrong_login_inputs}')
                self.show_login_lines()

    def login_validator(self, log_arg) -> bool:
        return log_arg.startswith('+') or ('@' in log_arg and '.com' in log_arg)

    def password_validator(self, pass_arg) -> bool:
        return len(pass_arg) >= 8

    def login_type(self, log_arg) -> str:
        if log_arg.startswith('+'):
            return 'phone_number'
        return 'email'
