# -*- coding:utf-8 -*-
__author__ = 'xuan'

from .configurations import *


class MongoConfig:
    def __init__(self, key):
        self.key = key
        self.__set_mongo_config()

    def __set_mongo_config(self):
        self.master_host = trader_config.get(self.key, 'master_host')
        self.slave_host = None
        self.user = trader_config.get(self.key, 'user')
        self.passwd = trader_config.get(self.key, 'password')
        self.db_name = trader_config.get(self.key, 'db_name')
        self.port = trader_config.get(self.key, 'port')

