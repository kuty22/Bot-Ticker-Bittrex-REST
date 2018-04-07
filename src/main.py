from Utils.yml import loadYaml
from Utils import NB_WORKER, BASE_CURRENCY
from Utils.worker import automate_worker
import os

def main():
    marketLstAvailable = loadYaml(os.path.dirname(".") + "config.yml")
    nb_worker = NB_WORKER
    workers = automate_worker(nb_worker, BASE_CURRENCY, marketLstAvailable)
    while True:
        workers.run()
        
if __name__ == '__main__':
    main()
