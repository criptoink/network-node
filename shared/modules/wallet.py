
import json

from pywallet import wallet
from shared.modules.cipher import decrypt_value, encrypt_value


class Account():
    def __init__(self, primal_hash):
        self.primal_hash = primal_hash


    def create_account(self):  
        
        seed = wallet.generate_mnemonic()
        w = wallet.create_wallet(network="BTC", seed=seed, children=0)
        with open('vault/ink.wallet.json', 'w') as f:        
            f.write(json.dumps({
                "ink_address": encrypt_value(self.primal_hash.encode('utf-8'), w["address"].encode('utf-8')),
                "ink_private_key": encrypt_value(self.primal_hash.encode('utf-8'), w["private_key"].encode('utf-8')),
                "ink_public_key": encrypt_value(self.primal_hash.encode('utf-8'), w["public_key"].encode('utf-8')),
            }))
        return Account.unlock_account(self)

    def unlock_account(self):    
        with open('vault/ink.wallet.json', 'r') as f:
            data = json.load(f)
        try:
            values = {}
            for key in data:
                values[key] = decrypt_value(self.primal_hash.encode('utf-8'), data[key]).decode("utf-8")
            del self.primal_hash
            return values
        except ValueError:
           print(f'Invalid password.')


