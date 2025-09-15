import json
import os
from datetime import datetime

class DatabaseManager:

    def __init__(self, file_path="online-banking-management-system/data/accounts.json"):
        """ Initialize the DatabaseManager.
        parameter file_path: Path to the JSON file used for storing accounts."""
        self.file_path = "online-banking-management-system/data/accounts.json"
        self.backup_dir = "online-banking-management-system/data/backup/"

    def initialize_database(self):
        """Create the database file with a default account if it does not exist.
        Ensures the project always has a base JSON file to work with."""
        try:
            if not os.path.exists(self.file_path):
                initial_data = {
                    "accounts": {
                        "ACC001": {
                            "account_number": "ACC001",
                            "pin": "1234",
                            "name": "Ravi",
                            "balance": 1500.00,
                            "account_type": "Savings",
                            "created_date": "2024-01-15",
                            "is_active": True
                        }
                    }
                }
            self.save_data(initial_data)
        except Exception as e:
            print(e)
    
    def load_data(self):
        """Load account data from the JSON file.
        return: Dictionary containing all account details."""
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            self.initialize_database()
            return self.load_data()
        except json.JSONDecodeError:
            print("Error: Database file corrupted.")
            return {}

    def save_data(self, data):
        """Save updated account data to the JSON file.
        A backup of the previous file is created before saving.
        parameter data: Dictionary containing account data."""
        try:
            self.backup_data()  # always backup before overwrite
            with open(self.file_path, "w") as f:
                json.dump(data, f, indent=4)
            print(f"Saved changes to {self.file_path}")
        except Exception as e:
            print(e)
    

    def backup_data(self):
        """Create timestamped backup of database file."""
        try:
            if not os.path.exists(self.backup_dir):
                os.makedirs(self.backup_dir)

            if os.path.exists(self.file_path):
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                backup_file = os.path.join(self.backup_dir, f"backup_{timestamp}.json")

                with open(self.file_path, "r") as file, open(backup_file, "w") as backup:
                    backup.write(file.read())
                print(f"Backup created at {backup_file}")
            else:
                print("No database file to backup")
        except Exception as e:
            print(e)
    

"""Testing the functions"""
# db_manager = DatabaseManager("accounts.json")
# db_manager.initialize_database()

# db_manager.backup_data()
