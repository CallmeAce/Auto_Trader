import pandas as pd
import numpy as np
import datetime


from dao.jqdata_web_dao import JQData

class FirstFilter(object):

    def __init__(self):
        jq_obj = JQData()

    def FirstFilter_PreOpen(self, stock_list, check_date):
        ret = []
        for stock in stock_list:
            #         tmp_history_df = attribute_history(stock, 180, unit='1d',fields=['open', 'close', 'high', 'low', 'volume', 'money','paused','pre_close','factor'],skip_paused=True, df=True, fq='pre')
            end_date = check_date.strftime("%Y-%m-%d")
            start_date = (check_date - datetime.timedelta(90)).strftime("%Y-%m-%d")
            price_df = self.jq_obj.get_price(stock, start_date=start_date, end_date=end_date, frequency='daily', fields=None,
                                 skip_paused=True, fq='pre', count=None, panel=True, fill_paused=True)
            if price_df.shape[0] < 40:
                continue

            extra_df = self.jq_obj.get_extras(info='is_st', security_list=stock, count=1, end_date=end_date)
            if extra_df.iloc[0][stock] == True:
                continue
            zumbie_ratio = (price_df['close'].max() - price_df['close'].min()) / price_df.iloc[-1]['close']
            if zumbie_ratio < 0.1:
                ret.append(stock)

        return ret
