import threading
import time

from server.interfaces.cripto_ink_server import CriptoInkServer
from server.server import Server


def server_threading():
    Server.cli(CriptoInkServer)

def client_threading():
    print('Start Client')
    print('=========================================')

if __name__ == '__main__':
    client = threading.Thread(target=client_threading)
    sever = threading.Thread(target=server_threading)

    client.start()
    time.sleep(4)
    sever.start()
