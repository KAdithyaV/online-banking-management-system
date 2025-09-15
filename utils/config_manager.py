import os
import json

class ConfigManager:
    """Simple config manager with JSON file persistence."""

    CONFIG_FILE = "online-banking-management-system/utils/config.json" 

    def __init__(self):
        """If the config file doesn't exist, creates it with default values"""
        try:
            if not os.path.exists(self.CONFIG_FILE):
                default_config = {
                "withdrawal_limit": 1000,
                "minimum_balance": 100,
                "max_transfer_amount": 5000 }
                with open(self.CONFIG_FILE, "w") as file:
                    json.dump(default_config, file)

        except Exception as e:
            print(e)           
                   

    def load_config(self):
        """Loads the configuration from the JSON file"""
        try:
             with open(self.CONFIG_FILE, "r") as file:
                  return json.load(file)
        except Exception as e:
            print(e)           
 

    def save_config(self, config):
        """Saves the given configuration dictionary to the JSON file"""
        try:
            with open(self.CONFIG_FILE, "w") as file:
                json.dump(config, file)

        except Exception as e:
            print(e)
            


    def get_withdrawal_limit(self):
        """Returns the current withdrawal limit from the config"""
        try:
            return self.load_config().get("withdrawal_limit")
        except Exception as e:
            print(e)  


    def get_minimum_balance(self):
        """Returns the current minimum balance requirement from the config"""
        try:
             return self.load_config().get("minimum_balance")
        except Exception as e:
            print(e) 
 


    def get_max_transfer_amount(self):
        """Returns the current maximum transfer amount from the config"""
        try:
            return self.load_config().get("max_transfer_amount")
        except Exception as e:
            print(e)
            
        


    def update_config(self, key, value):
        """Updates a specific key in the config file with a new value"""
        try:
            config = self.load_config()
            config[key] = value
            self.save_config(config)
        except Exception as e:
            print(e)    
        

# c = ConfigManager()
# print("Min balance:", c.get_minimum_balance())
# c.update_config("minimum_balance", 200)
# print("Updated Min balance:", c.get_minimum_balance())
