import csv
import datetime
import json
import random
import string

import os
import requests
import sqlite3

from flask import Flask, make_response
from flask import request

# app = Flask('app')
app = Flask(__name__)


####################
@app.route('/')
def hello():
    return 'Hello'


####################
@app.route('/now')
def now():
    return str(datetime.datetime.now())


####################
"""
@app.route('/get-requirements')
def get_requirements():
    try:
        f = open('requirements.txt', 'r') 
        # ...
        # <--- exception
    except Exception as ex:
        pass
    finally:
        f.close()
"""


@app.route('/get-requirements')
def get_requirements():
    # with open('requirements.txt', 'r') as f:
    #     result = f.read()
    # print(result)
    # result = result.replace('\n', '<br>')
    # print(result)
    # return result
    with open('requirements.txt', 'r') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader]
        # str_rows = '<br>'.join([
        #     str(record)
        #     for record in rows
        # ])
    print(rows)
    print(type(rows))
    return str(rows)


####################
@app.route('/gen-password')
def gen_password():
    # """ If argument length --- obiazatelnyy my hotim"""
    # if 'length' not in request.args:
    #     return make_response('Missing argument "length", 400')
    # length = int(request.args['length'])
    DEFAULT_LENGTH = 10
    length = int(request.args.get('length', DEFAULT_LENGTH))
    # return ''.join([
    #     random.choice(string.ascii_lowercase)
    #     for _ in range(length)
    # ])
    digits = int(request.args.get('digit', 0))
    specials = int(request.args.get('specials', 0))
    generation_symbols = string.ascii_lowercase

    if digits == 1:
        generation_symbols += string.digits
    if specials == 1:
        generation_symbols += '!@#$%^&*('

    return ''.join([
        random.choice(generation_symbols)
        for _ in range(length)
    ])


####################
@app.route('/get-astronauts')
def get_astronauts():
    response = requests.get('http://api.open-notify.org/astros.json')
    if response.status_code == 200:
        # text = response.content
        print(type(response.text), response, )
        resp = json.loads(response.text)
        print(type(resp))
        return f'Austranauts number: {resp["number"]}'
        # return f'Austranauts number: {resp.get("number", '<N/A>')}'
    else:
        return f'Error {response.status_code}'


####################
@app.route('/get-customers')
def get_customer():
    query = 'SELECT FirstName, LastName FROM customers WHERE City = "Oslo" or City = "Paris"'
    records = execute_query(query)
    result = '<br>'.join([
        str(record)
        for record in records
    ])
    return result


@app.route('/get-customers-st-bad')
def get_customer_st():
    state = request.args.get('state', '')
    query = f'SELECT FirstName, LastName FROM customers WHERE State = "{state}"'  # <--- bad solving,
    # http://localhost:8080/get-customers-st-bad?state=CA" UNION ALL select BillingAddress, Total from invoices --
    # http://localhost:8080//get-customers-st-bad?state=CA%22%20UNION%20ALL%20select%20BillingAddress,%20Total%20from%20invoices%20--
    # !!! sql in'ektsiya !!!
    records = execute_query(query)
    result = '<br>'.join([
        str(record)
        for record in records
    ])
    return result


@app.route('/get-customers-st-good')
def get_customers():
    state = request.args.get('state', '')
    query = 'SELECT FirstName, LastName FROM customers WHERE State = ?'
    records = execute_query(query, state)
    result = '<br>'.join([
        str(record)
        for record in records
    ])
    return result


# def execute_query(query, *args):
#     db_path = os.path.join(os.getcwd(), 'chinook.db')
#     conn = sqlite3.connect(db_path)
#     cur = conn.cursor()
#     cur.execute(query, args)
#     records = cur.fetchall()
#     return records


def execute_query(query, *args):
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(query, args)   # tut  args  -- tuple  !!!!
    records = cur.fetchall()
    return records


@app.route('/get-revenue')
def get_revenue():
    query = 'SELECT sum(UnitPrice*Quantity) FROM invoice_items'
    records = execute_query(query)
    # result = '<br>'.join([
    #     str(record)
    #     for record in records
    # ])
    result = str(records[0][0])  # records here is 1 element(len=1) so use without join !!!!!
    return result


app.run(host="localhost", port=8080, debug=True)
