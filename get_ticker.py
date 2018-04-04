from bittrex.bittrex import Bittrex, API_V2_0
import yaml
import datetime
import time
from multiprocessing import Pool


def loadYaml():
    with open('result.yml', 'r') as yaml_file:
        res = yaml.load(yaml_file)
        return res

def get_ticker_from_market_list(marketList):
    my_bittrex = Bittrex(None, None)  # or defaulting to v1.1 as Bittrex(None, None)
    for market in marketList:

        print(my_bittrex.get_ticker(market), "  / {}".format(market))

def createWorker(nb_worker, marketList):
    workers = [[] for e in range(nb_worker)]
    # for worker in range(nb_worker):
    #     workers
    i = 0
    while i < len(marketList):
        for worker in range(nb_worker):
            if i is len(marketList):
                break
            # print(res_btc[i - 1])
            workers[worker].append(marketList[i])
            i += 1

    pool = Pool(nb_worker)
    pool.map(get_ticker_from_market_list, workers)
    return workers

def main():

    res = loadYaml()
    start = datetime.datetime.now()
    nb_workers = 4
    res_btc = res["BTC"]
    workers = createWorker(nb_workers, res_btc)
    # for worker in range(nb_workers):
        # workers
    # print(workers)
    # i = 0
    # while i < len(res_btc):
    #     for worker in range(nb_workers):
    #         if i is len(res_btc):
    #             break
    #         # print(res_btc[i - 1])
    #         workers[worker].append(res_btc[i])
            # i += 1
    print("len worker :", len(workers))
    print("len row 0 :", len(workers[0]))
    print("len row 1 :", len(workers[1]))
    print("len row 2 :", len(workers[2]))
    print("len row 3 :", len(workers[3]))
    # for market in res_btc:
    end = datetime.datetime.now()
    print("There are {} markets available for the BaseCurrency".format(len(res_btc)))
    print("time to execute a get_ticker on each baseCurrency BTC market {}".format(time.mktime(end.timetuple())
- time.mktime(start.timetuple())))
if __name__ == '__main__':
    main()
