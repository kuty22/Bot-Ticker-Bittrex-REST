from multiprocessing import Pool
from .broker import automate_broker

class automate_worker:

    def __init__(self, nb_worker, baseCurrency, marketListAll):
        marketList = marketListAll[baseCurrency]
        workers = [[] for e in range(nb_worker)]
        i = 0
        while i < len(marketList):
            for worker in range(nb_worker):
                if i is len(marketList):
                    break
                workers[worker].append(marketList[i])
                i += 1
        self.__nbWorker = nb_worker
        self.__pool = Pool(nb_worker)
        self.__workers = workers


    def run(self):
        self.__pool.map(automate_broker.get_ticker_from_market_list, self.__workers)
