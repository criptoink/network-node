import json
import random
import socket
import string

from jsonrpclib import Server


def get_verification_token():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(32))
    return result_str


payload = {
    "whoiam": {
        "host": socket.gethostbyname(socket.gethostname()),
        "owner": "1Dfuy6XgAWaDz7z8tcFeDPvtxnDNmY6UvU",  # Get From WalletHandle
        "verification_token": get_verification_token()
    },
    "body": "Hello Neighbor"
}

json_object = json.dumps(payload, indent=4)


def main():
    conn = Server('http://127.0.1.1:3420')
    print('+++++++++++++ handShake +++++++++++++++')
    print(conn.handShake(json_object))


if __name__ == '__main__':
    main()
