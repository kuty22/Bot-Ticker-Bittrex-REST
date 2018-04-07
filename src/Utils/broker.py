from bittrex.bittrex import Bittrex, API_V2_0
from .database import automate_db

class automate_broker:

    def get_ticker_from_market_list(marketList):
        my_bittrex = Bittrex(None, None)
        dB = automate_db()
        for market in marketList:
            ticker = my_bittrex.get_ticker(market)
            if ticker and ticker["success"] is True:
                ticker = ticker["result"]

                dB.insert_ticker(dict({
                "marketName": market,
                "baseCurrency": market.split("-")[0],
                "bid": ticker["Bid"],
                "ask": ticker["Ask"],
                "last": ticker["Last"]}))
