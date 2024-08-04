import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import datetime
plt.style.use('seaborn-v0_8')

stock = yf.Ticker("EQNR")

print(stock.income_stmt)
data = stock.income_stmt
x = stock.income_stmt.columns


plt.gca().xaxis.axis_date
plt.ylabel('Billions of USD')
plt.plot(x, data.loc['Total Revenue'] / 1000000000, linestyle='solid', label='Total Revenue', color='blue')
plt.plot(x, data.loc['Normalized EBITDA'] / 1000000000, linestyle='solid', label='EBITDA', color='green')
plt.plot(x, data.loc['Operating Income'] / 1000000000, linestyle='solid', label='Operating Income', color='black')
plt.plot(x, data.loc['Net Income'] / 1000000000, linestyle='dashed', label='Net Income', color='black')
plt.plot(x, data.loc['Total Expenses'] / 1000000000, linestyle='dashed', label='Total Expenses', color='grey')
plt.legend(loc='best')
plt.title('Company Performance')

plt.show()