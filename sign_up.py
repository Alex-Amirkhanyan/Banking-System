import sys
import random
import hashlib
import getpass
from connect_to_database import my_cursor, my_db


class AddUserToDb:
    def __init__(self, name_arg, surname_arg, age_arg, email_arg, phone_number_arg, password_arg):
        self.name = name_arg
        self.surname = surname_arg
        self.age = age_arg
        self.email = email_arg
        self.phone_number = phone_number_arg
        self.password = password_arg
        self._card_number = None
        self._account_number = None
        self._create_account()

    def _create_account(self):
        self._card_number = self._generate_card_number()
        self._account_number = self._generate_account_number()
        sql_command = f"INSERT INTO client_list (name, surname, age, email, phone_number, card_number, account_number, " \
                      f"password, money_amount, loan_amount) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        user_info = [(self.name, self.surname, self.age, self.email, self.phone_number, self._card_number,
                      self._account_number, self.password, 0, 0)]
        my_cursor.executemany(sql_command, user_info)
        my_db.commit()
        print('Your account has been successfully created. Here are your card number and account number details.')
        print(f'\nCard number: {self._card_number}        Account number: {self._account_number}')

    def _generate_card_number(self) -> int:
        account_type = 'card_number'
        while True:
            generated_card_number = 0
            for _ in range(16):
                digit = random.randint(0, 9)
                generated_card_number = generated_card_number * 10 + digit
            if self._check_card_account_number_availability(account_type, generated_card_number):
                return generated_card_number

    def _generate_account_number(self) -> int:
        account_type = 'account_number'
        while True:
            generated_account_number = 0
            for _ in range(14):
                digit = random.randint(0, 9)
                generated_account_number = generated_account_number * 10 + digit
            if self._check_card_account_number_availability(account_type, generated_account_number):
                return generated_account_number

    def _check_card_account_number_availability(self, account_type_arg, card_num) -> bool:
        sqlCommand = f"SELECT * FROM client_list WHERE {account_type_arg} = '{card_num}'"
        my_cursor.execute(sqlCommand)
        res = my_cursor.fetchall()
        if len(res) > 0:
            return False
        return True


class SignUp:
    def __init__(self):
        self._wrong_tries = 0
        self._name = None
        self._surname = None
        self._age = None
        self._email = None
        self._phone_number = None
        self._password = None
        self._check_add_email()

    def _check_add_email(self):
        email_inp = input('Write your email please: ')
        if self._wrong_tries == 9:
            print('Too many wrong inputs, try again later.')
            sys.exit()

        if self._validate_email(email_inp) and self._check_if_user_exists(email_inp, 'email'):
            self._email = email_inp
            self._wrong_tries = 0
            self._check_add_phone()
        else:
            self._wrong_tries += 1
            self._check_add_email()

    def _check_add_phone(self):
        number_inp = input('Write your number please: ')
        if self._wrong_tries == 9:
            print('Too many wrong inputs, try again later.')
            sys.exit()

        if self._validate_number(number_inp) and self._check_if_user_exists(number_inp, 'phone_number'):
            self._phone_number = number_inp
            self._wrong_tries = 0
            self._check_add_name()
        else:
            self._wrong_tries += 1
            self._check_add_phone()

    def _check_add_name(self):
        name_inp = input('Write your name please: ')
        if self._wrong_tries == 9:
            print('Too many wrong inputs, try again later.')
            sys.exit()

        if self._validate_name_surname(name_inp, 'Name'):
            self._name = name_inp
            self._wrong_tries = 0
            self._check_add_surname()
        else:
            self._wrong_tries += 1
            self._check_add_name()

    def _check_add_surname(self):
        surname_inp = input('Write your surname please: ')
        if self._wrong_tries == 9:
            print('Too many wrong inputs, try again later.')
            sys.exit()

        if self._validate_name_surname(surname_inp, 'Surname'):
            self._surname = surname_inp
            self._wrong_tries = 0
            self._check_add_age()
        else:
            self._wrong_tries += 1
            self._check_add_surname()

    def _check_add_age(self):
        age_inp = input('Write your age please: ')
        if self._wrong_tries == 4:
            print('Too many wrong inputs, try again later.')
            sys.exit()

        if self._validate_age(age_inp):
            self._age = int(age_inp)
            self._wrong_tries = 0
            self._check_add_password()
        else:
            self._wrong_tries += 1
            self._check_add_age()

    def _check_add_password(self):
        password_inp = getpass.getpass('Write your password please (min. 8 characters): ')
        if self._wrong_tries == 9:
            print('Too many wrong inputs, try again later.')
            sys.exit()

        if self._validate_password(password_inp):
            self._password = hashlib.sha224(password_inp.encode()).hexdigest()
            AddUserToDb(self._name, self._surname, self._age, self._email, self._phone_number, self._password)
        else:
            self._wrong_tries += 1
            self._check_add_password()

    def _validate_name_surname(self, searchable_arg, searchable_arg_type) -> bool:
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

    def _validate_age(self, age_arg) -> bool:
        if not age_arg.isdigit():
            print('Age must contain only numbers')
            return False
        age_arg = int(age_arg)
        if age_arg < 18:
            print('You must be at least 18 years old.')
            return False
        if age_arg > 100:
            print('Age cannot be greater than 100.')
            return False
        return True

    def _validate_email(self, email_arg) -> bool:
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

    def _validate_number(self, number_arg) -> bool:
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

    def _validate_password(self, password_arg) -> bool:
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

    def _check_if_user_exists(self, searchable_arg, searchable_arg_type):
        arg_type = 'email'
        if searchable_arg_type == 'phone_number':
            arg_type = 'phone number'

        sql_command = f"SELECT * FROM client_list WHERE {searchable_arg_type} = '{searchable_arg}'"
        my_cursor.execute(sql_command)
        res = my_cursor.fetchall()
        if len(res) > 0:
            print(f'\nUser already exists, either log in or try writing another {arg_type}.\n')
            sys.exit()
        return True
