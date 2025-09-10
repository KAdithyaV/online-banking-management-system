import os
import json
from database_manager import db_manager

class Accountrepository:
    def __init__(self,db_manager):
        self.db_manager = db_manager
    
    def create_account(self,account_data):
        data = self.db_manager.load_data()
        acc_no = account_data["account_number"]
        data["accounts"][acc_no] = account_data
        self.db_manager.save_data(data)
    
    def get_account(self, account_number):
        data = self.db_manager.load_data()
        return data["accounts"].get(account_number)

    def update_account(self, account_number, updated_data):
        data = self.db_manager.load_data()
        if account_number in data["accounts"]:
            data["accounts"][account_number].update(updated_data)
            self.db_manager.save_data(data)
    
    def delete_account(self, account_number):
        data = self.db_manager.load_data()
        if account_number in data["accounts"]:
            data["accounts"][account_number]["is_active"] = False
            self.db_manager.save_data(data)
            return True   # success
        return False      # account not found


    def get_all_accounts(self):
        data = self.db_manager.load_data()
        return data["accounts"]
    
    def account_exists(self, account_number):
        data = self.db_manager.load_data()
        return account_number in data["accounts"]

#create backup files
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
# account_repo.create_account(account_data)
# print("Account created ")

# # Fetch account
# acc = account_repo.get_account("ACC002")
# print("Fetched account:", acc)

# # Update account
# account_repo.update_account("ACC001", {"is_active": True})
# print("Updated account:", account_repo.get_account("ACC001"))

# Delete (deactivate) account
# account_repo.delete_account("ACC001")



