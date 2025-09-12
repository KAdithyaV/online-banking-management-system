# import accounts.json from data
import json

class BankingSystem:

    MIN_BALANCE = 100.0
    WITHDRAWAL_LIMIT = 5000.0

    FILENAME="/Users/adithyavardhankode/Documents/Adithya/Career/Data_Engineering/PythonPractice/online-banking-management-system/data/accounts.json"

    def __init__(self, current_user, database_manager):
        self.current_user = None
        self.database_manager = database_manager

    self.database_manager.initialize_database()

    def load_data(self, FILENAME):
        try:
            with open(FILENAME,"r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return None 
    
    def authenticate_user(self):
        """To authenticate the user"""
        print("\n=== Login ===")
        acc_no = input("Account Number: ").strip()
        pin = input("PIN: ").strip()
        jsonData = self.load_data(self.FILENAME)
        acc_numbers = list(jsonData["accounts"].keys())
        if acc_no in acc_numbers:
            if pin == jsonData["accounts"][acc_no]["pin"]:
                print(f"Welcome, {jsonData["accounts"][acc_no]["name"]}!")
                return True
        else:
            print("Invalid user")
            return False

    def create_account():
        pass

    def main_menu(self):
        if not self.current_user:
            print("Please login first.")
            return

        while self.current_user:
            print("\n===== ONLINE BANKING SYSTEM =====")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Transfer Money")
            print("5. Transaction History")
            print("6. Account Details")
            print("7. Logout")
            print("8. Exit")

            choice = input("Choose an option (1-8): ").strip()
            try:
                if choice == "1":
                    bal = self.current_user.check_balance()
                    print(f"Current Balance: {self.fmt.format_currency(bal)}")

                elif choice == "2":
                    self._deposit()

                elif choice == "3":
                    self._withdraw()

                elif choice == "4":
                    self.transfer_money()

                elif choice == "5":
                    self._show_transactions()

                elif choice == "6":
                    self.fmt.print_account_summary(self.current_user.get_account_info())

                elif choice == "7":
                    self.logout()

                elif choice == "8":
                    print("Goodbye!")
                    self.database_manager.backup_data()
                    exit(0)
                else:
                    print("Invalid option.")
            except (ValidationError, InsufficientFundsError) as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

    def transfer_money():
        pass

    def logout():
        pass

    def run():
        pass

bs = BankingSystem("ACC001", "1234")    
    
success = bs.authenticate_user()
main_menu("ACC001")