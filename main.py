import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('seaborn-v0_8')
stock = yf.Ticker("EQNR")

df = stock.dividends

data = df.resample('YE').sum()


plt.xlabel('Years')
plt.ylabel('Dividend payed out (USD)')
plt.bar(data.index.year, data.values, label='Dividends (USD)')

plt.show()