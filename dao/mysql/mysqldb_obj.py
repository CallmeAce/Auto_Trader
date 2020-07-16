import pandas as pd
import pymysql
import logging

pymysql.install_as_MySQLdb()
from config.mysql_config import MysqlConfig

from sqlalchemy import create_engine

logger = logging.getLogger(__file__)

class MysqlDBObject(MysqlConfig):

    def __init__(self, key):
        super().__init__(key)

    def get_table_engine(self,tab_name):

