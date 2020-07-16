from jqdatasdk import *
import pandas as pd
import seaborn as sb
import numpy as np
from config.configurations import *

class JQData(object):

    def __init__(self):
        id = trader_config.get('jq_auth', 'id')
        passwd = trader_config.get('jq_auth', 'password')

        # auth(trader_config.get('jq_auth','id'),trader_config.get('jq_auth','password'))
        auth(id,passwd)

    def check_auth(self):
        return is_auth()


    def check_quota(self):
        return get_query_count()


    def get_all_securities(self):
        return get_all_securities()

if __name__ == "__main__":
    jq_obj = JQData()
    print(is_auth())
    print(jq_obj.check_quota())
    # print(jq_obj.get_all_securities())