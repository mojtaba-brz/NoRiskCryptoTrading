from kucoin.client import Market

import numpy as np
import matplotlib.pyplot as plt

url = "https://api.kucoin.com"

# # Strategy Tester
sym = "OUSD-USDT"
market = Market(url = url)
data = np.array(market.get_kline(symbol = sym, kline_type = "1day"), dtype = "float")

close = np.flip(data[:,2])
Open  = np.flip(data[:,2-1])
high  = np.flip(data[:,2+1])
low   = np.flip(data[:,2+2])

sell_limit_1 = np.average(close) + np.std(close)
buy_limit_1 = np.average(close) - np.std(close)

sell_limit_2 = np.average(close) + 2*np.std(close)
buy_limit_2 = np.average(close) -  2*np.std(close)


