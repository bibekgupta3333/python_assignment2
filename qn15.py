# 15. Imagine you are designing a banking application. What would a
# customer look like? What attributes would she have? What methods
# would she have?


class Bank:

    def __init__(self, user_id, balance):
        self.balance = balance
        self.user_id = user_id

    def log_in(self, user_id):
        user_ids = [1, 2, 3, 4, 5, 6]
        if user_id in user_ids:
            print('enter into account')
        else:
            return False

    def deposit(self, user_id, amount):
        self.log_in(user_id)
        print(f'{amount} is deposit to you account')
        self.balance = self.balance+amount
        print(f'your current balance is {self.balance}')
        print(f'{self.user_id} id user is logout from bank')

    def withdraw(self, user_id, amount):
        self.log_in(user_id)
        if self.balance > 0 and self.balance > amount:
            print(f'you withdraw Rs {amount}')
            self.balance = self.balance-amount
            print(f'your current balance is {self.balance}')
        else:
            print(f'you less balance than given {amount}')
            print(f'your current balance is {self.balance}')
        print(f'{self.user_id} id user is logout from bank')


if __name__ == "__main__":
    bank = Bank(1, 10000)
    bank.deposit(1, 20000)
    bank.withdraw(1, 20000)
