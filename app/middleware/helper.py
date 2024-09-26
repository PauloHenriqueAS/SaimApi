"""
app/Repositorys/configDb.py

This module contains database configurations.
"""

import json

class HelperSaim:
    def get_salt_data(self): 
        with open('../config.json', 'r') as config_file:
            config_data = json.load(config_file)

        SaltData = config_data["salt_encrpty"]
        print(SaltData)
        return SaltData

helper = HelperSaim()