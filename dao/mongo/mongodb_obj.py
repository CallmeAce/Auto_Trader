__author__ = 'xuan'

import atexit
import sys
from signal import *
from pymongo import *
from config.mongo_config import MongoConfig
from pymongo import MongoClient

class MongoDBObject(MongoConfig):

    def __init__(self, key):
        super().__init__(key)
        self.mongodb = MongoClient(
            'mongodb://%s:%s@%s:%s/%s' % (self.user, self.passwd, self.master_host, self.port, self.db_name))

    def get_collection(self,collection_name):
        return self.mongodb[self.db_name][collection_name]

mongo_db = MongoDBObject("mongo_auto_trader")
