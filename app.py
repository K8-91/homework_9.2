import json
import csv
from flask import Flask
from flask import request, redirect
from flask import render_template

with open('bank.json', "r") as jsonfile:
    bank_py = json.load(jsonfile)

rates_to_CSV = bank_py['rates']

currency_rates = {}

for item in rates_to_CSV:
    currency_rates[item['code']] = item



rates_keys = rates_to_CSV[0].keys()
with open("bank.csv", 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, delimiter =';', fieldnames= rates_keys)
    dict_writer.writeheader()
    dict_writer.writerows((rates_to_CSV))


app = Flask(__name__)

@app.route('/currency', methods = ['GET', 'POST'])
def currency():
    if request.method == 'GET':
        return render_template("currency.html")
    if request.method == 'POST':
        data = request.form
        currency = data['currency']
        quantity = float(data['quantity'])
        if currency_rates.get(currency):
            result = currency_rates[currency]['ask'] * quantity
            return render_template("currency.html", result=result)


if __name__=="__main__":
    app.run()


