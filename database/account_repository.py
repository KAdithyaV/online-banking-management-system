import os
import json
from datetime import datetime
from database_manager import db_manager

class Accountrepository:
    """ Repository layer for handling CRUD operations on accounts.
    Uses DatabaseManager for reading/writing JSON database. """
    def __init__(self,db_manager): 
        """Initialize AccountRepository with a DatabaseManager instance."""
        self.db_manager = db_manager
    
    def create_account(self,name, pin, account_type, initial_balance=0.0):
        """Create a new account and save it in the database.
        parameter account_data: Dictionary containing account details."""
        try:
            data = self.db_manager.load_data()
            acc_no = account_data["account_number"]
            data["accounts"][acc_no] = account_data
            self.db_manager.save_data(data)
        except Exception as e:
            print(e)
    
    def get_account(self, account_number):
        """Fetch account details by account number.
        parameter account_number: The account number (str).
        return: Dictionary of account details or None if not found."""
        try:
            data = self.db_manager.load_data()
            return data["accounts"].get(account_number)
        except Exception as e:
            print(e)
    

    def update_account(self, account_number, updated_data):
        """Update existing account details.
        parameter account_number: Account number to update.
        parameter updated_data: Dictionary with fields to update."""
        try:
            data = self.db_manager.load_data()
            if account_number in data["accounts"]:
                data["accounts"][account_number].update(updated_data)
                self.db_manager.save_data(data)
        except Exception as e:
            print(e)
    
    def delete_account(self, account_number):
        """Deactivate an account (soft delete).
        parameter account_number: Account number to deactivate.
        return: True if deactivated, False if account not found."""
        try:
            data = self.db_manager.load_data()
            if account_number in data["accounts"]:
                data["accounts"][account_number]["is_active"] = False
                self.db_manager.save_data(data)
                return True   # success
            return False      # account not found
        except Exception as e:
            print(e)

    def get_all_accounts(self):
        """Retrieve all accounts in the database.
        return: Dictionary of all accounts."""
        try:
            data = self.db_manager.load_data()
            return data["accounts"]
        except Exception as e:
            print(e)
    
    
    def account_exists(self, account_number):
        """Check if an account exists.
        parameter account_number: Account number to check.
        return: True if exists, False otherwise."""
        try:
            data = self.db_manager.load_data()
            return account_number in data["accounts"]
        except Exception as e:
            print(e)
    
"""Testing the functions"""

account_repo = Accountrepository(db_manager)
# transaction_repo = TransactionRepository(db_manager)

account_data = {
    "account_number": "ACC002",
    "pin": "1289",
    "name": "Joe",
    "balance": 10000.0,
    "account_type": "Savings",
    "created_date": "2025-09-08",
    "is_active": True
}


# # Create account
account_repo.create_account(account_data)
print("Account created ")

# # Fetch account
# acc = account_repo.get_account("ACC002")
# print("Fetched account:", acc)

# # Update account
account_repo.update_account("ACC002", {"name": "Eren"})
print(f"Updated account: {account_repo.get_account("ACC002")}")

# Delete (deactivate) account
# account_repo.delete_account("ACC001")



