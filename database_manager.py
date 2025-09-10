import json
import os
from datetime import datetime

class DatabaseManager:

    def __init__(self, file_path="accounts.json"):
        self.file_path = file_path
        self.backup_dir = "data/backup/"

    def initialize_database(self):
        if not os.path.exists(self.file_path):
            initial_data = {
                "accounts": {
                    "ACC001": {
                        "account_number": "ACC001",
                        "pin": "1234",
                        "name": "John Doe",
                        "balance": 1500.00,
                        "account_type": "Savings",
                        "created_date": "2024-01-15",
                        "is_active": True
                    }
                }
            }
            self.save_data(initial_data)

    def load_data(self):
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
        self.backup_data()  # always backup before overwrite
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    def backup_data(self):
        """Create timestamped backup of database file."""
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

db_manager = DatabaseManager("accounts.json")
db_manager.initialize_database()
db_manager.backup_data()
