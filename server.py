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

# import pin controller
from periphery import GPIO


app = Flask(__name__)
wallet = Wallet()
#payment = Payment(app, wallet)

PRICE_PER_BEAN = 20000
SECONDS_PER_BEAN = 2

total_sold = 0
    
def get_price_from_request(request):
    qty = request.args.get('qty')
    return PRICE_PER_BEAN*qty

# buy jellybeans. price depends on qty requested
@app.route('/buy')
@payment.required(get_price_from_request)
def purchase():

    qty = request.args.get('qty')
    total_sold += int(qty)
    
    # Open GPIO 6 with output direction
    gpio_out = GPIO(6, "out")

    # dispense some beans
    gpio_out.write(True)

    # This needs to be calibrated depending 
    # on dispenser speed. 
    time.sleep(2*qty)

    # Stop spitting out beans
    gpio_out.write(False)
    gpio_out.close()

    return "Paid %d. Please collect your jellybeans." % get_price_from_request

# get total number sold
@app.route('/total')
def total():
    return "A total of %d beans have been purchased." % total_sold

if __name__ == '__main__':
    app.run(host='0.0.0.0')