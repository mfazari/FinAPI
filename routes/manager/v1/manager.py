import json
import urllib
import yfinance as yf

from flask import Flask, Blueprint
from services.services import manager_service


manager_page = Blueprint("manager_page", __name__, template_folder="templates")


@manager_page.route("/v1/manager/search/<search_name>", methods=["GET"])
def get_organization_by_symbol(search_name):
    data = manager_service.get_organization_by_symbol(search_name)
    return data


@manager_page.route("/v1/manager/stock/<symbol>", methods=["GET"])
def get_chart_data_by_symbol(symbol):
    data = manager_service.get_chart_data(symbol)
    return data
