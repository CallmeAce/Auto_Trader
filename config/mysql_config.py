# -*- coding:utf-8 -*-
__author__ = 'chen xi'
from .configurations import *


class MysqlConfig:
    def __init__(self, config_name):
        self.__get_configurations(config_name)

    def __get_configurations(self, config_name):
        self.host = trader_config.get(config_name, 'host')
        self.user = trader_config.get(config_name, 'user')
        self.passwd = trader_config.get(config_name, 'password')
        self.db_name = trader_config.get(config_name, 'db_name')
        self.port = trader_config.get(config_name, 'port')
