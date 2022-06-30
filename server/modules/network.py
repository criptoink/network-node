import socket
from contextlib import closing

from server.functions.criptoink import hand_shake
from server.functions.nodes import (get_node_forbidden_list, get_node_in_list,
                             get_node_out_list)
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer


def who_i_am(instance):
    return {
        "host": socket.gethostbyname(socket.gethostname()),
        "port": find_free_port(),
        "owner": instance.wallet["ink_address"]
    }


def find_free_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]

def cripto_ink_server(instance):
    instance.server = SimpleJSONRPCServer((instance.who_i_am["host"], instance.who_i_am["port"]))

    # Register Functions
    instance.server.register_function(hand_shake)
    instance.server.register_function(get_node_in_list)
    instance.server.register_function(get_node_out_list)
    instance.server.register_function(get_node_forbidden_list)
    instance.db.init('vault/' + instance.wallet["ink_address"] + '.db', passphrase=instance.wallet['ink_private_key'])
    print(f'Cripto.Ink Node Start at {instance.who_i_am["host"]}:{instance.who_i_am["port"]}')
    instance.server.serve_forever()
    instance.db.close()


    return instance.server
