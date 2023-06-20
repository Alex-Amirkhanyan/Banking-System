import sys
import datetime
from login import InputLoginValidator
from sign_up import SignUp


class MainClass:
    def __init__(self):
        self.bank_name = 'Liberty National Bank'
        self.greet_user()

    def greet_user(self):
        current_hour = datetime.datetime.now().hour
        if 5 <= current_hour < 12:
            greeting = 'Good morning!'
        elif 12 <= current_hour < 18:
            greeting = 'Good afternoon!'
        else:
            greeting = 'Good evening!'
        self.show_actions(greeting)

    def show_actions(self, textArg):
        print(f'{textArg} Welcome to {self.bank_name}.')
        login_text = f'\033[38;2;0;201;87m[1] Log in\033[0m'
        signup_text = f'\033[38;2;205;51;51m[2] Sign up\033[0m'
        print(f'\n{login_text}               {signup_text}')
        self._input_action_answer(0)

    def _input_action_answer(self, counter):
        count = counter
        choices = ['1', '2']
        inp = input('\nWrite the number of your choice here: ')

        if inp in choices:
            if int(inp) == 1:
                self._user_login()
            else:
                self._user_signup()
        else:
            count += 1
            if count == 3:
                print('Try again several minutes later.')
                sys.exit()
            else:
                print('\n\033[91mYour inserted answer is not right, write again.\033[0m\n')
                self._input_action_answer(count)

    def _user_login(self):
        InputLoginValidator()

    def _user_signup(self):
        SignUp()


MainClass()
