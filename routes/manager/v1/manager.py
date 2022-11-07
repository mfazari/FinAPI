import json
import urllib
from flask import Flask, Blueprint
import yfinance as yf

manager_page = Blueprint("manager_page", __name__, template_folder="templates")


@manager_page.route("/v1/manager/search/<symbol>", methods=["GET"])
def get_stock_by_symbol(symbol):
    response = urllib.request.urlopen(
        f"https://query2.finance.yahoo.com/v1/finance/search?q={symbol}"
    )
    content = response.read()
    stock_data = json.loads(content)

    data = []
    for x in range(len(stock_data["quotes"])):
        temp_dict = {
            "name": stock_data["quotes"][x]["longname"],
            "symbol": stock_data["quotes"][x]["symbol"],
        }
        data.append(temp_dict)
        # data[x]["symbol"] = stock_data["quotes"][x]["symbol"]

    return data
