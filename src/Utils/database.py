# Database class
import pymysql
import logging
from . import MYSQL__USER, MYSQL__PASSWORD, MYSQL__DATABASE, MYSQL__HOST


class automate_db:

    def __init__(self):
        self.dBConnect()

    def dBConnect(self):
        try:
            self.__cnx = pymysql.connect(user=MYSQL__USER, password=MYSQL__PASSWORD,
                                         host=MYSQL__HOST, database=MYSQL__DATABASE,
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)
            self.__cursor = self.__cnx.cursor()

            logging.debug("DataBase connected")

        except pymysql.Error as err:
            logging.error("tradingBotDB connections failed: {}".format(err))

    def selectDatabase(self, sql, args=None):
        if args is not None:
            self.__cursor.execute(sql, args)
        else:
            self.__cursor.execute(sql)
        tab_return = []
        # free mysql cursor and make the return variable
        for c in self.__cursor:
            tab_return.append(c)
        return tab_return

    # execute the sql requests and comit change.(data must be an array)
    def pushDataBase(self, sql, data=None):
        try:
            if data is None:
                self.__cursor = self.__cnx.cursor()
                self.__cursor.execute(sql)
                self.__cnx.commit()
                return self.__cursor.lastrowid
            else:
                self.__cursor = self.__cnx.cursor()
                self.__cursor.execute(sql, data)
                self.__cnx.commit()
                return self.__cursor.lastrowid
        except pymysql.Error as err:
            logging.error("tradingBotDB: pushDataBase failed: {}".format(err))

########################
# ------requests-------#
########################

    def insert_ticker(self, ticker):
        sql = "INSERT INTO ticker(marketName, baseCurrency, bid, ask, last)\
               VALUES(\"{}\", \"{}\", \"{}\", \"{}\", \"{}\");".format(
               ticker["marketName"], ticker["baseCurrency"],
               ticker["bid"], ticker["ask"], ticker["last"])

        return self.pushDataBase(sql)
