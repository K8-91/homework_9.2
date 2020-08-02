import json
import csv

with open('bank.json', "r") as jsonfile:
    bank_py = json.load(jsonfile)

rates_to_CSV = (bank_py['rates'])


rates_keys = rates_to_CSV[0].keys()
with open("bank.csv", 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, delimiter =';', fieldnames= rates_keys)
    dict_writer.writeheader()
    dict_writer.writerows((rates_to_CSV))

from flask import Flask
from flask import request, redirect
from flask import render_template


app = Flask(__name__)

@app.route('/currency', methods = ['GET', 'POST'])
def currency():
    if request.method == 'GET':
        return render_template("currency.html")
    if request.method == 'POST':
        data = request.form
        currency = data.get['currency']
        quantity = float(data.get['quantity'])
        for item in rates_to_CSV:
            if currency == item['code']:
                result = quantity * item['ask']
                return result

if __name__=="__main__":
    app.run(debug=True)

