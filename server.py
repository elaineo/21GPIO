import os 
import json
import requests

import sqlite3
from flask import g

# import from the 21 Developer Library
from two1.lib.wallet import Wallet
from two1.lib.bitserv.flask import Payment

# import flask web microframework
from flask import Flask
from flask import request

import subprocess 

app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

PRICE_PER_BEAN = 10000
SECONDS_PER_BEAN = 2

total_sold = 0
    
def get_price_from_request(request):
    qty = int(request.args.get('qty'))
    return PRICE_PER_BEAN*qty

# buy jellybeans. price depends on qty requested
@app.route('/buy')
@payment.required(get_price_from_request)
def purchase():

    qty = int(request.args.get('qty'))
    total_sold += qty
    
    # drive GPIO#6 (pin 1)
    subprocess.call("sudo python3 gpio_controller.py %d %d" % (6, SECONDS_PER_BEAN*qty), shell=True)

    return "Paid %d. Please collect your jellybeans." % qty

# get total number sold
@app.route('/total')
def total():
    return "A total of %d beans have been purchased." % total_sold

if __name__ == '__main__':
    app.run(host='0.0.0.0')
