import getpass
from pathlib import Path

from rich.console import Console
from rich.prompt import Confirm
from shared.modules.database import (create_node_in_connection,
                                     create_node_out_connection, db,
                                     run_migrate)
from shared.modules.wallet import Account

from server.modules.network import cripto_ink_server, who_i_am


def get_password():
    p = getpass.getpass(prompt='Enter password ')
    return p


class Server:

    def cli(CriptoInkServer):
        CriptoInkServer.console = {
            'terminal': Console(),
            'ask': Confirm(),

        }
        CriptoInkServer.wallet = Server.wallet_handle(CriptoInkServer)
        CriptoInkServer.db = Server.db_handle(CriptoInkServer)
        CriptoInkServer.who_i_am = who_i_am(CriptoInkServer)
        CriptoInkServer.server = cripto_ink_server(CriptoInkServer)

    def connect_genesis_node(CriptoInkServer):
        CriptoInkServer.console['terminal'].print("Save Genesis Node in Connections List")
        create_node_out_connection(
            'genesis.cripto.ink',
            '1Dfuy6XgAWaDz7z8tcFeDPvtxnDNmY6UvU'
        )
        create_node_in_connection(
            'genesis.cripto.ink',
            '1Dfuy6XgAWaDz7z8tcFeDPvtxnDNmY6UvU'
        )

    def new_database(CriptoInkServer):
        CriptoInkServer.console['terminal'].print("💾 Setup Storage for new Account...")
        db.init('vault/' + CriptoInkServer.wallet["ink_address"] + '.db', passphrase=CriptoInkServer.wallet['ink_private_key'])
        run_migrate()
        connect_genesis_node = CriptoInkServer.console['ask'].ask("[yellow]Connect to genesis.cripto.ink? [/yellow]⚠️ ")
        if connect_genesis_node is True:
            Server.connect_genesis_node(CriptoInkServer)
        db.close()
        return db

    def load_database(CriptoInkServer):
        CriptoInkServer.console['terminal'].print("💾 Load Storage...")
        db.init('vault/' + CriptoInkServer.wallet["ink_address"] + '.db', passphrase=CriptoInkServer.wallet['ink_private_key'])
        db.close()
        return db

    def db_handle(CriptoInkServer):
        db_file = Path('vault/' + CriptoInkServer.wallet["ink_address"] + '.db')
        if db_file.is_file():
            return Server.load_database(CriptoInkServer)
        else:
            return Server.new_database(CriptoInkServer)

    def load_wallet(CriptoInkServer):
        CriptoInkServer.console['terminal'].print(
            f'[bold]vault/ink.wallet.json [yellow]FOUND[/yellow]✔️.[/bold] Unlocking INK account...')
        Server.ask_to_continue(CriptoInkServer)
        p = get_password()
        CriptoInkServer.console['terminal'].print(f'👥 Unlocking [bold] CRIPTO INK [/bold]account...')
        run_time_account = Account(p)
        return run_time_account.unlock_account()

    def new_wallet(CriptoInkServer):
        CriptoInkServer.console['terminal'].print(
            f'[bold]vault/ink.wallet.json [red]NOT FOUND[/red]❌.[/bold] Creating new account...')
        Server.ask_to_continue(CriptoInkServer)
        p = get_password()
        CriptoInkServer.console['terminal'].print(f'👥Creating a new INK account...')
        run_time_account = Account(p)
        return run_time_account.create_account()

    def wallet_handle(CriptoInkServer):
        file = Path('vault/ink.wallet.json')
        if file.is_file():
            return Server.load_wallet(CriptoInkServer)
        else:
            return Server.new_wallet(CriptoInkServer)

    def ask_to_continue(CriptoInkServer):
        ask = CriptoInkServer.console['ask'].ask("[yellow]Continue?[/yellow]⚠️")
        if ask is False:
            CriptoInkServer.console['terminal'].print('[bold]Bye!👋[/bold]')
            exit()
