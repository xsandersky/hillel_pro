from flask import Flask, request, jsonify
from hw_7 import Card
import psycopg2
import os


app = Flask(__name__)

conn = psycopg2.connect(
    host = '127.0.0.1',
    port = '5432',
    dbname = 'bank_cards',
    user = 'vitalii',
    password = os.environ.get('DB_PASSWORD', '1325')
)


@app.route('/card', methods=['POST'])
def create_card():
    data = request.get_json()
    number = data['number']
    cvv = data['cvv']
    issue = data['issue']
    expiration = data['expiration']
    status = data['status']
    balance = data['balance']

    card = Card()
    card.save_to_db(number, cvv, issue, expiration, status, balance)

    return jsonify({'message': 'Card created successfully'}), 201


@app.route('/card/<number>', methods=['GET'])
def get_card(number):
    card = Card()
    record = card.get_by_number(number)

    b_id = record[0][0]
    b_number = record[0][1]
    b_cvv = record[0][2]
    b_issue = record[0][3]
    b_expiration = record[0][4]
    b_balance = record[0][5]
    b_status = record[0][6]

    card.disconnect()

    return f'id = {b_id} | number = {b_number} | cvv = {b_cvv} | issue = {b_issue} |\
            expiration = {b_expiration} | balance = {b_balance} | \
            status = {b_status}', 200


if __name__ == '__main__':
    app.run()
