import os
import sqlite3
from typing import List, Set

def profit_by_invoice_items():
    db_pass = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_pass)
    cur = connection.cursor()
    records = cur.execute('SELECT UnitPrice * Quantity FROM invoice_items').fetchall()
    cur.close()
    sum = 0
    for rec in records:
        sum += rec[0]

    return sum

# print(get_profit())


def repeat_first_name():
    db_pass = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_pass)
    cur = connection.cursor()
    records = cur.execute('SELECT FirstName from customers').fetchall()
    cur.close()

    dct = {}

    for rec in records:
        name = rec[0]
        if name not in dct:
            dct[name] = 1
        else:
            dct[name] += 1

    for key, val in dct.items():
        if val > 1:
            print(key, val)

# repeat_first_name()

def get_customers(state_name=None, city_name=None) -> None:
    db_pass = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_pass)
    cur = connection.cursor()

    query_sql = '''
        SELECT FirstName
              ,City 
              ,State
          FROM customers
        '''
    filter_query = ''
    if city_name and state_name:
        filter_query = f" WHERE City = '{city_name}' and State = '{state_name}'"
    if city_name and not state_name:
        filter_query = f" WHERE City = '{city_name}'"
    if state_name and not city_name:
        filter_query = f" WHERE State = '{state_name}'"

    query_sql += filter_query
    record = cur.execute(query_sql).fetchall()
    cur.close()

    return record