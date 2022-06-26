import getpass
from pathlib import Path

from peewee import OperationalError

from modules.database import (Feeds, NodeConnections, connectGenesisNode, db,
                              getNodesList)
from modules.wallet import Account


def getpassword():
    p = getpass.getpass(prompt='Enter password ')
    return p

def walletHandle():
    file = Path('vault/ink.wallet.json')

    if file.is_file():
        print(f'vault/ink.wallet.json found. Unlocking INK account...')
        p = getpassword()
        inkAccount = Account.unlock_account(p)
    else:
        print(f'vault/ink.wallet.json not found. Creating new account...')
        p = getpassword()
        inkAccount = Account.create_account(p)
    
    return inkAccount


def dbHandle(wallet):
    dbFile = Path('vault/'+wallet["ink_address"]+'.db')
    if dbFile.is_file():
        pass
    else:
        db.init('vault/'+wallet["ink_address"]+'.db', passphrase=wallet['ink_private_key'])
        try:
            NodeConnections.create_table()
            print("'NodeConnections' storage created successfully!")
        except OperationalError:
            print("'NodeConnections' storage already exists!")
        try:
            Feeds.create_table()
            print("'Feeds' storage created successfully!")
        except OperationalError:
            print("'Feeds' storage already exists!")

        db.close()

def GenerisNodesHandle(wallet):
    dbFile = Path('vault/'+wallet["ink_address"]+'.db')
    if dbFile.is_file():
        db.init('vault/'+wallet["ink_address"]+'.db', passphrase=wallet['ink_private_key'])
        connectGenesisNode()
        nodes = getNodesList()
        print("[Nodes List]")
        for node in nodes:
            print ("host: {} owner: {} join_at: {}".format(node.host, node.owner, node.join_at))
        db.close()



if __name__ == '__main__':
    wallet = walletHandle()
    dbHandle(wallet)
    GenerisNodesHandle(wallet)

    


