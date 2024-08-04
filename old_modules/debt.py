import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from matplotlib.dates import num2date

plt.style.use('seaborn-v0_8')

stock = yf.Ticker("EQNR")
data = stock.balance_sheet

x = data.columns


print(data.head(50))
plt.gca().xaxis.axis_date
plt.ylabel('Billions of USD')
plt.plot(x, data.loc['Net Debt'] / 1000000000, linestyle='solid', label='Net Debt', color='blue')
plt.plot(x, data.loc['Total Debt'] / 1000000000, linestyle='solid', label='Total Debt', color='black')
plt.legend(loc='upper right')
plt.title('Company Debt')

plt.show()