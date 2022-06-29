import socket
from contextlib import closing

from functions.base import handShake
from functions.nodes import getNodeForbidenList, getNodeInList, getNodeOutList
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

from modules.database import db


def find_free_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]

def CriptoInkServer(wallet):
    port = find_free_port()
    server = SimpleJSONRPCServer(('localhost', 3420))
    db.init('vault/'+wallet["ink_address"]+'.db', passphrase=wallet['ink_private_key'])
    #Register Functions
    server.register_function(handShake)
    server.register_function(getNodeInList)
    server.register_function(getNodeOutList)
    server.register_function(getNodeForbidenList)      
    #Register Functions
    print(f"Cripto.Ink Node Start at port:{port}...")
    server.serve_forever()
    db.close()
