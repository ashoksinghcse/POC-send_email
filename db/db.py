import redis
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv('.env')

Base = declarative_base()


class Db:
    __conn = None



    def make_connection(self):
        if self.__conn is None:
            try:
                DB_USERNAME = os.getenv('USER_NAME')
                DB_PASSWORD = os.getenv('PASSWORD')
                DB_HOST = os.getenv('HOST_NAME')
                DB_NAME = os.getenv('DB_NAME')
                self.__conn = 'mysql+pymysql://{user}:{password}@{server}/{database}'.format(
                    user=DB_USERNAME,
                    password=DB_PASSWORD,
                    server=DB_HOST,
                    database=DB_NAME,
                    auth_plugin='mysql_native_password'
                )
            except Exception as e:
                print(str(e))
        return self.__conn
