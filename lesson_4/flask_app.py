from flask import Flask, request
from hw_4 import get_customers
import sqlite3
import os


app = Flask(__name__)


@app.route('/customers', methods=['GET'])
def get_customers_view():
    state_name = request.args.get('state_name', '')
    city_name = request.args.get('city_name', '')
    customers = get_customers(state_name, city_name)
    return customers


if __name__ == '__main__':
    app.run()
