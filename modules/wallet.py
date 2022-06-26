import json
from pprint import pprint

from pywallet import wallet

from modules.cipher import decrypt_value, encrypt_value


class Account():

    def create_account(password):  
        print(f'Creating a new INK account...')
        seed = wallet.generate_mnemonic()
        w = wallet.create_wallet(network="BTC", seed=seed, children=0)
        print(f'network address is {w["address"]}')
        with open('vault/ink.wallet.json', 'w') as f:        
            f.write(json.dumps({
                "ink_address": encrypt_value(password.encode('utf-8'), w["address"].encode('utf-8')),
                "ink_private_key": encrypt_value(password.encode('utf-8'), w["private_key"].encode('utf-8')),
                "ink_public_key": encrypt_value(password.encode('utf-8'), w["public_key"].encode('utf-8')),
            }))
        return Account.unlock_account(password)

    def unlock_account(password):    
        with open('vault/ink.wallet.json', 'r') as f:
            data = json.load(f)
        try:
            values = {}
            for key in data:
                values[key] = decrypt_value(password.encode('utf-8'), data[key]).decode("utf-8")
            print(f'Unlocking INK account...')
            print(f'network address is {values["ink_address"]}')
            return values
        except ValueError:
           print(f'Invalid password.')
