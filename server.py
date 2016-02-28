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
payment = Payment(app, wallet)

PRICE_PER_BEAN = 20000
    
def get_price_from_request(request):
    qty = request.args.get('qty')
    return PRICE_PER_BEAN*qty

# Open GPIO 6 with output direction
gpio_out = GPIO(6, "out")

gpio_out.write(1)

gpio_out.close()

# buy jellybeans. price depends on qty requested
@app.route('/buy')
@payment.required(get_price_from_request)
def purchase():
    # dispense some beans

    return "Paid %d. Please collect your jellybeans." % get_price_from_request


if __name__ == '__main__':
    app.run(host='0.0.0.0')