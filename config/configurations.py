# -*- coding:utf-8 -*-
__author__ = 'xuan'

import os
import configparser

root = os.path.dirname(__file__)


class TraderConfig(object):
    def __init__(self, method=None):
        """
        输入 test 或者是 prod
        :param method:
        :return:
        """
        if method != 'test' and method != "prod" and method != "stage":
            method = self.get_status()
        config = configparser.ConfigParser()
        config.read_file(open("{0}/{1}/default.cfg".format(root, method)))
        self.config = config

    def get(self, key: object, field: object) -> object:
        return self.config.get(key, field)

    def get_status(self):
        # 判断本机是ubuntu还是mac
        cmd = 'uname -s'
        r = os.popen(cmd)
        name = r.read()
        status = 'prod' if 'Linux' in name else 'test'
        r.close()
        return status

trader_config = TraderConfig(os.getenv('ENV', 'test'))

# print(mbafc_config.get('mongo_elements_local_test','user'))
