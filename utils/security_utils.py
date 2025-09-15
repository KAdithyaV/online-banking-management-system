
import time
import random

class SecurityUtils:
    """Security and ID generation helpers."""
    @staticmethod
    def encrypt_pin(pin):
        """ Encrypts' a PIN by shifting each digit by +3 (mod 10).
        Example: 1234 -> 4567 """
        try:
            return ''.join(str((int(d) + 3) % 10) for d in str(pin))
        except Exception as e:
            print(f"Error encrypting PIN: {e}")
            return ""
    
    @staticmethod
    def decrypt_pin(encrypted_pin):
        """Reverses the encrypt_pin operation by shifting digits -3 (mod 10).
        Example: 4567 -> 1234"""
        try:
             return ''.join(str((int(d) - 3) % 10) for d in str(encrypted_pin))
        except Exception as e:
            print(f"Error decrypting PIN: {e}")
            return ""
       
    
    @staticmethod
    def generate_account_number():
        """Generates a random 10-digit account number as a string."""
        try:
            return str(random.randint(10**9, 10**10 - 1))
        except Exception as e:
            print(f"Error generating account number: {e}")
            return "0000000000"

        
    
    @staticmethod
    def generate_transaction_id():
        """Creates a unique transaction ID using the current timestamp (YYYYMMDDHHMMSS)
            followed by a random 4-digit number
            Example: '20250911143022' + '4823' => '202509111430224823'"""
        try:
            timestamp = time.strftime("%Y%m%d%H%M%S")
            return f"{timestamp}{random.randint(1000, 9999)} "
        except Exception as e:
            print(f"Error generating transaction ID: {e}")
            return "0000000000000000"
    

    @staticmethod
    def hash_password(password):
        """Generates a simple numeric hash of a password by summing ASCII values of characters.
        Example: 'abc' -> ord('a') + ord('b') + ord('c') = 97 + 98 + 99 = 294 """
        try:
            return str(sum(ord(c) for c in password))
        except Exception as e:
            print(f"Error hashing password: {e}")
            return "0"


# s = SecurityUtils()
# acc_no = s.generate_account_number()
# print("Account No:", acc_no)
# txn_id = s.generate_transaction_id()
# print("Transaction ID:", txn_id)




