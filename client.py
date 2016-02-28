import json
import os

# import from the 21 Developer Library
from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests

# Jellybean client!
wallet = Wallet()
username = Config().username
requests = BitTransferRequests(wallet, username)

# server address
SERVER_URL = 'http://localhost:5000/'

def cmd_buy(qty):
    url = SERVER_URL + 'buy?qty=%s' % qty
    r = requests.get(url)
    print(r.text)

if __name__ == '__main__':
    if len(sys.argv) == 0:
        print('Please enter a valid quantity')
    else:
        cmd_buy(int(sys.argv[0]))