import json
import yfinance as yf
import urllib


class ManagerService:
    def get_organization_by_symbol(self, search_name):
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

            return data

    def get_chart_data(self, symbol):
        data_pandas = yf.download(tickers=symbol, period='3mo', interval='1d', rounding=True)
        data_dict = json.loads(data_pandas.to_json(orient='table'))
        data_dict["max_high"] = max(data_pandas.High)
        data_dict["min_high"] = min(data_pandas.High)
        return data_dict

    def get_news(self, symbol):
        symbol_data = yf.Ticker(symbol)
        news_data = symbol_data.get_news()
        return news_data

manager_service = ManagerService()
