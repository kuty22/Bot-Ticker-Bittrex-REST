from bittrex.bittrex import Bittrex, API_V2_0
import yaml

def create_save(baseCurrency, marketAvailable):
    yamlObject = dict({"baseCurrency": baseCurrency})
    with open('result.yml', 'w') as yaml_file:
        yaml.dump(yamlObject, yaml_file, default_flow_style=False)
        yaml.dump(marketAvailable, yaml_file, default_flow_style=False)


def main():
    my_bittrex = Bittrex(None, None)  # or defaulting to v1.1 as Bittrex(None, None)
    markets = my_bittrex.get_markets()
    btcMarket = []
    if markets is None or markets["result"] is None:
        return
    markets = markets["result"]
    BaseCurrencyList = []
    tickerByBaseCurrency = dict({})
    for market in markets:
        if market["BaseCurrency"] not in BaseCurrencyList:
            BaseCurrencyList.append(market["BaseCurrency"])
            tickerByBaseCurrency[market["BaseCurrency"]] = []
        if market["BaseCurrency"] == "BTC":
            btcMarket.append(market["MarketName"])

    for market in markets:
        tickerByBaseCurrency[market["BaseCurrency"]].append(market["MarketName"])

    # for e in btcMarket:
    #     print(e)
    create_save(BaseCurrencyList, tickerByBaseCurrency)
    print("list of base currency available: {}".format(BaseCurrencyList))
    print("number of market available on Bittrex is {}".format(len(btcMarket)))
if __name__ == '__main__':
    main()
