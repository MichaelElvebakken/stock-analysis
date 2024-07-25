import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('seaborn-v0_8')
stock = yf.Ticker("EQNR")
print(stock.balance_sheet)

df = stock.dividends

#Resize the data to consist of 2 columns with each row representing one year
data = pd.DataFrame(df.resample('YE').sum())
data.reset_index(inplace=True)
data['Year'] = data['Date'].dt.year

plt.xlabel('Years')
plt.ylabel('Dividend payed out (USD)')
plt.bar(data['Year'], data['Dividends'], label='Dividends (USD)')

plt.show()

