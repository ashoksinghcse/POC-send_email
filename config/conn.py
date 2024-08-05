import os
import mysql.connector
from logger import Logger

class Db:
    __conn = None
    def connect_db(self):
        if self.__conn is None:
            try:
                self.__conn = mysql.connector.connect(
                    host=os.getenv('HOST_NAME'),
                    database=os.getenv('DB_NAME'),
                    user=os.getenv('USER_NAME'),
                    password=os.getenv('PASSWORD')
                )
            except Exception as e:
                print(str(e))
        return self.__conn

class MailModel(Db):
    __conn = None
    def __init__(self):
        self.__conn = Db().connect_db()
        self.logger = Logger(self.__class__.__name__).get()

    def insert_data(self,data,table):
        try:
            curs = self.__conn.cursor(dictionary=True)
            print(data.keys())
            column = data.keys()
            col = ",".join([str(s) for s in column])
            values = tuple(data.values())
            query = f"INSERT INTO {table} ({col}) VALUES {values}"
            curs.execute(query)
            self.__conn.commit()
        except Exception as e:
            self.logger.exception(str(e))