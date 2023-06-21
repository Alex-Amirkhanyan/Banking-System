from loan_operations import GetLoan, PayLoan
from change_account_details import ChangeAccountDetails
from money_operations import ShowBalance, WithdrawMoney, DepositMoney


class PostLoginOperations:
    def __init__(self, user_data_arg):
        self._wrong_tries = 0
        self._name = user_data_arg[0][0]
        self._surname = user_data_arg[0][1]
        self._age = user_data_arg[0][2]
        self._email = user_data_arg[0][3]
        self._phone_number = user_data_arg[0][4]
        self._card_number = user_data_arg[0][5]
        self._account_number = user_data_arg[0][6]
        self._money_amount = user_data_arg[0][7]
        self._loan_amount = user_data_arg[0][8]
        self.__password = user_data_arg[0][9]
        print(f'Welcome back {self._name}, what do you intend to do?')
        self.show_options()

    def show_options(self):
        print('\n[1] Show Balance        [2] Change account details\n[3] Withdraw money      [4] Deposit money\n'
              '[5] Get loan            [6] Pay loan')
        inp = input('Write your answer here: ')
        self.validate_input(inp)

    def validate_input(self, inp_arg):
        match inp_arg:
            case '1':
                ShowBalance(self._money_amount, self._loan_amount, self._card_number, self._account_number)
            case '2':
                ChangeAccountDetails(self._name, self._surname, self._phone_number, self._email, self.__password)
            case '3':
                WithdrawMoney(self._email, self.__password, self._money_amount, self._card_number, self._account_number)
            case '4':
                DepositMoney(self._email, self.__password, self._money_amount)
            case '5':
                GetLoan(self._money_amount, self._loan_amount, self._email, self.__password)
            case '6':
                PayLoan(self._money_amount, self._loan_amount, self._email, self.__password)
            case _:
                print('Wrong input, you need to write one of the following numbers: 1, 2, 3, 4, 5 or 6.')
                self.show_options()
