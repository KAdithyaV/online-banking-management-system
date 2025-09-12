import data
import database
import tests
import utils

class BankAccount:
    def __init__(self, account_number, pin, name, balance, account_type, created_date, is_active):
        self.account_number = account_number
        self.pin = pin
        self.name = name
        self.balance = balance
        self.account_type = account_type
        self.created_date = created_date
        self.is_active = is_active

    def deposit(self, amount):
        if amount is None or amount <= 0:
            print("Amount must be positive.")
        self.balance = round(self.balance + float(amount), 2)
        return self.balance

    def withdraw(amount):
        pass

    def check_balance():
        pass

    def get_account_info():
        pass

    def validate_pin(pin):
        pass

    def is_account_active():
        pass
