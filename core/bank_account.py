"""
BankAccount
-----------
Represents a bank account with deposit/withdraw methods.
Each method has internal try/except to handle errors gracefully.
"""

from datetime import datetime


class BankAccount:
    def __init__(self, account_number, pin, name, balance,
                 account_type="Savings", created_date=None, is_active=True):
        self.account_number = account_number
        self._pin = pin
        self.name = name
        self.balance = balance
        self.account_type = account_type
        self.created_date = created_date or datetime.now().strftime("%Y-%m-%d")
        self.is_active = is_active

    def deposit(self, amount):
        """Deposit money with error handling."""
        try:
            if amount <= 0:
                raise ValueError("Deposit must be positive.")
            self.balance += amount
            print(f"Deposited {amount}. New balance = {self.balance}")
            return self.balance
        except Exception as e:
            print("Error in deposit:", e)
            return self.balance

    def withdraw(self, amount: float, minimum_balance: float, daily_limit: float):
        """Withdraw money enforcing rules, handled inside."""
        try:
            if amount <= 0:
                raise ValueError("Withdrawal must be positive.")
            if amount > daily_limit:
                raise ValueError(f"Exceeds daily withdrawal limit {daily_limit}.")
            if self.balance - amount < minimum_balance:
                raise ValueError(f"Insufficient funds. Min balance = {minimum_balance}")
            self.balance -= amount
            print(f"Withdrew {amount}. New balance = {self.balance}")
            return self.balance
        except Exception as e:
            print("Error in withdrawal:", e)
            return self.balance

    def check_balance(self):
        print(f"Balance = {self.balance}")
        return self.balance

    def get_account_info(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance,
            "account_type": self.account_type,
            "created_date": self.created_date,
            "is_active": self.is_active,
        }

    def validate_pin(self, pin: str):
        return self._pin == pin

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "pin": self._pin,
            "name": self.name,
            "balance": self.balance,
            "account_type": self.account_type,
            "created_date": self.created_date,
            "is_active": self.is_active,
        }

    @staticmethod
    def from_dict(d: dict):
        return BankAccount(
            d["account_number"], d["pin"], d["name"],
            d["balance"], d["account_type"], d["created_date"], d["is_active"]
        )
