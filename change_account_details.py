import sys
import hashlib
import getpass
from connect_to_database import my_cursor, my_db


class ValidatorClass:
    def validate_name_surname(self, searchable_arg, searchable_arg_type) -> bool:
        if not searchable_arg:
            print(f'\n{searchable_arg_type} field cannot be empty.')
            return False
        elif len(searchable_arg) < 2:
            print(f'\n{searchable_arg_type} is too short, it must contain at least 2 characters.')
            return False
        elif len(searchable_arg) > 50:
            print(f'\n{searchable_arg_type} is too long, it must not contain more than 50 characters.')
            return False
        elif not searchable_arg.isalpha():
            print(f'\n{searchable_arg_type} can only contain letters.')
            return False
        return True

    def validate_email(self, email_arg) -> bool:
        if not email_arg:
            print('Email field cannot be empty.')
            return False
        elif '@' not in email_arg:
            print('Email must contain the \'@\' symbol.')
            return False
        elif '.' not in email_arg:
            print('Email must contain a domain name (e.g. \'gmail.com\', \'yahoo.com\', \'outlook.com\').')
            return False
        return True

    def validate_number(self, number_arg) -> bool:
        if not number_arg.startswith('+'):
            print('Phone number must start with \'+\' and country code.')
            return False
        if not number_arg[1:].isdigit():
            print('Phone number must start with \'+\' and contain only numbers.')
            return False
        if len(number_arg) < 4:
            print('Number is too short')
            return False
        if len(number_arg) > 15:
            print('Number is too long')
            return False
        return True

    def validate_password(self, password_arg) -> bool:
        if len(password_arg) < 8:
            print('Password is too short.')
            return False
        if not any(char.isupper() for char in password_arg):
            print('Password must contain at least one uppercase letter.')
            return False
        if not any(char.islower() for char in password_arg):
            print('Password must contain at least one lowercase letter.')
            return False
        if not any(char.isdigit() for char in password_arg):
            print('Password must contain at least one digit.')
            return False
        return True


class ChangeAccountDetails:
    def __init__(self, name_arg, surname_arg, phone_number_arg, email_arg, password):
        self._wrong_tries = 0
        self._name = name_arg
        self._surname = surname_arg
        self._phone_number = phone_number_arg
        self._email = email_arg
        self.__password = password
        self.change_account_details()

    def change_account_details(self):
        inp = getpass.getpass('Write your password again please: ')
        if hashlib.sha224(inp.encode()).hexdigest() == self.__password:
            self._wrong_tries = 0
            self.change_account_details_options()
        else:
            self._wrong_tries += 1
            if self._wrong_tries == 3:
                print('Too many wrong attempts, try again later.')
                sys.exit()
            print(f'Wrong password, try again. Attempts left: {3 - self._wrong_tries}')
            self.change_account_details()

    def change_account_details_options(self):
        choices = ['1', '2', '3', '4', '5']
        print('\nWhat would you like to change? \n[1] Name\n[2] Surname\n[3] Email\n[4] Phone number\n[5] Password')
        inp = input('Write your answer here: ')
        if inp in choices:
            self._wrong_tries = 0
            self._validate_account_details_input(int(inp))
        else:
            self._wrong_tries += 1
            if self._wrong_tries == 4:
                print('Too many wrong attempts, try again later. ')
                sys.exit()
            print(
                f'\nYou have to write one of the following numbers: 1, 2, 3, 4 or 5. Try again. Attempts left: '
                f'{10 - self._wrong_tries}\n')
            self.change_account_details_options()

    def _validate_account_details_input(self, key_arg):
        dct = {1: 'name', 2: 'surname', 3: 'email', 4: 'phone number', 5: 'password'}
        if dct[key_arg] == 'password':
            inp = getpass.getpass(f'\nPlease write your new {dct[key_arg]}: ')
        else:
            inp = input(f'\nPlease write your new {dct[key_arg]}: ')
        dct = {1: 'name', 2: 'surname', 3: 'email', 4: 'phone_number', 5: 'password'}
        match dct[key_arg]:
            case 'name':
                if ValidatorClass().validate_name_surname(inp, 'Name'):
                    if inp == self._name:
                        print(f'\nYour name is already {self._name}.')
                        self._wrong_tries += 1
                        if self._wrong_tries == 4:
                            print('\nToo many wrong attempts, try again later.')
                            sys.exit()
                        self._validate_account_details_input(1)
                    else:
                        self._wrong_tries = 0
                        self._update_sql_details(dct[key_arg], inp, 'name')
                else:
                    self._wrong_tries += 1
                    if self._wrong_tries == 4:
                        print('\nToo many wrong attempts, try again later.')
                        sys.exit()
                    self._validate_account_details_input(1)
            case 'surname':
                if ValidatorClass().validate_name_surname(inp, 'Surname'):
                    if inp == self._surname:
                        print(f'\nYour surname is already {self._surname}.')
                        self._wrong_tries += 1
                        if self._wrong_tries == 4:
                            print('\nToo many wrong attempts, try again later.')
                            sys.exit()
                        self._validate_account_details_input(2)
                    else:
                        self._wrong_tries = 0
                        self._update_sql_details(dct[key_arg], inp, 'surname')
                else:
                    self._wrong_tries += 1
                    if self._wrong_tries == 4:
                        print('\nToo many wrong attempts, try again later.')
                        sys.exit()
                    self._validate_account_details_input(2)
            case 'email':
                if ValidatorClass().validate_email(inp):
                    if inp == self._email:
                        print(f'\nYour email is already {self._email}.')
                        self._wrong_tries += 1
                        if self._wrong_tries == 4:
                            print('\nToo many wrong attempts, try again later.')
                            sys.exit()
                        self._validate_account_details_input(3)
                    else:
                        self._wrong_tries = 0
                        self._update_sql_details(dct[key_arg], inp, 'email')
                else:
                    self._wrong_tries += 1
                    if self._wrong_tries == 4:
                        print('\nToo many wrong attempts, try again later.')
                        sys.exit()
                    self._validate_account_details_input(3)
            case 'phone_number':
                if ValidatorClass().validate_number(inp):
                    if inp == self._phone_number:
                        print(f'\nYour phone number is already {self._phone_number}.')
                        self._wrong_tries += 1
                        if self._wrong_tries == 4:
                            print('\nToo many wrong attempts, try again later.')
                            sys.exit()
                        self._validate_account_details_input(4)
                    else:
                        self._wrong_tries = 0
                        self._update_sql_details(dct[key_arg], inp, 'phone number')
                else:
                    self._wrong_tries += 1
                    if self._wrong_tries == 4:
                        print('\nToo many wrong attempts, try again later.')
                        sys.exit()
                    self._validate_account_details_input(4)
            case 'password':
                if ValidatorClass().validate_password(inp):
                    if hashlib.sha224(inp.encode()).hexdigest() == self.__password:
                        print('\nOld and new password cannot be the same.')
                        self._wrong_tries += 1
                        if self._wrong_tries == 4:
                            print('\nToo many wrong attempts, try again later.')
                            sys.exit()
                        self._validate_account_details_input(5)
                    else:
                        self._wrong_tries = 0
                        self._update_sql_details(dct[key_arg], inp, 'password')
                else:
                    self._wrong_tries += 1
                    if self._wrong_tries == 4:
                        print('\nToo many wrong attempts, try again later.')
                        sys.exit()
                    self._validate_account_details_input(5)


    def _update_sql_details(self, updatable_arg, new_value_arg, updatable_arg_name):
        try:
            self._update_sql_details_do_sql(updatable_arg, new_value_arg)
            if updatable_arg_name == 'password':
                print('Your password has been successfully updated. Please restart the program to continue.')
            else:
                print(f'Your {updatable_arg_name} has been successfully updated to "{new_value_arg}". '
                      f'Please restart the program to continue.')
        except Exception as e:
            print(f'An error occurred while updating the SQL details: {str(e)}. Try again.')

    def _update_sql_details_do_sql(self, updatable_arg, new_value_arg):
        sql_command = f"UPDATE client_list SET {updatable_arg} = %s WHERE email = %s AND password = %s"
        values = (new_value_arg, self._email, self.__password)
        my_cursor.execute(sql_command, values)
        my_db.commit()
