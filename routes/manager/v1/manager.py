import json
import urllib
from flask import Flask, Blueprint
import yfinance as yf

manager_page = Blueprint("manager_page", __name__, template_folder="templates")


@manager_page.route("/v1/manager/search/<search_name>", methods=["GET"])
def get_organization_by_symbol(search_name):
    response = urllib.request.urlopen(
        f"https://query2.finance.yahoo.com/v1/finance/search?q={search_name}"
    )
    content = response.read()
    stock_data = json.loads(content)

    data = []
    for x in range(len(stock_data["quotes"])):
        temp_dict = {
            "id": x,
            "name": stock_data["quotes"][x]["longname"],
            "symbol": stock_data["quotes"][x]["symbol"],
        }
        data.append(temp_dict)
        # data[x]["symbol"] = stock_data["quotes"][x]["symbol"]

    return data


@manager_page.route("/v1/manager/stock/<symbol>", methods=["GET"])
def get_stock_by_symbol(symbol):
    data = yf.download(tickers=symbol, period='3mo', interval='1d', rounding=True)
    print(data)
    dict = data.to_json(orient='table')

    return dict
