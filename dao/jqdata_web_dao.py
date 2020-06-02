from jqdatasdk import *
import pandas as pd
import seaborn as sb
import numpy as np
from config.configurations import *

class JQData(object):

    def __init__(self):
        auth(trader_config.get('jq_auth','id'),trader_config.get('jq_auth','password'))


    def check_auth(self):
        return is_auth()



if __name__ == "__main__":
    jq_obj = JQData()
    jq_obj.check_auth()



