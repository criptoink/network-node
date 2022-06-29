import getpass
import imp
from pathlib import Path

from rich.console import Console
from rich.prompt import Confirm

from modules.database import (createInNodeConnection, createOutNodeConnection,
                              db, runMigrate)
from modules.network import CriptoInkServer
from modules.wallet import Account


class CriptoInk ():
    def cli():
        console = {
            'terminal': Console(),
            'ask': Confirm()
            }
        wallet = CriptoInk.walletHandle(console)
        CriptoInk.dbHandle(wallet,console)
        CriptoInkServer(wallet)


    def dbHandle(wallet, console):
        def connectGenesisNode(): 
            console['terminal'].print("Save Genesis Node in Connections List")   
            createOutNodeConnection(
                'genesis.cripto.ink',
                '1Dfuy6XgAWaDz7z8tcFeDPvtxnDNmY6UvU'
            )
            createInNodeConnection(
                'genesis.cripto.ink',
                '1Dfuy6XgAWaDz7z8tcFeDPvtxnDNmY6UvU'
            )

        dbFile = Path('vault/'+wallet["ink_address"]+'.db')
        if dbFile.is_file():
            pass
        else:
            console['terminal'].print("💾 Setup Storage for new Account...")
            db.init('vault/'+wallet["ink_address"]+'.db', passphrase=wallet['ink_private_key'])
            runMigrate()
            askToConnectGenesisNode = console['ask'].ask("[yellow]Connect to genesis.cripto.ink? [/yellow]⚠️ ")
            if askToConnectGenesisNode is True:
                connectGenesisNode()
            db.close()
    
    def walletHandle(console):
        file = Path('vault/ink.wallet.json')
        if file.is_file():
            console['terminal'].print(f'[bold]vault/ink.wallet.json [yellow]FOUND[/yellow]✔️.[/bold] Unlocking INK account...')
            CriptoInk.askToContinue(console)
            p = CriptoInk.getpassword()
            console['terminal'].print(f'👥 Unlocking [bold] CRIPTO INK [/bold]account...')
            inkAccount = Account.unlock_account(p)
        else:
            console['terminal'].print(f'[bold]vault/ink.wallet.json [red]NOT FOUND[/red]❌.[/bold] Creating new account...')
            CriptoInk.askToContinue(console)
            p = CriptoInk.getpassword()
            console['terminal'].print(f'👥Creating a new INK account...')
            inkAccount = Account.create_account(p)
        
        return inkAccount

    def getpassword():
        p = getpass.getpass(prompt='Enter password ')
        return p

    def askToContinue(console):
        askToContinue = console['ask'].ask("[yellow]Continue?[/yellow]⚠️")
        if askToContinue is False:
            console['terminal'].print('[bold]Bye!👋[/bold]')
            exit();






