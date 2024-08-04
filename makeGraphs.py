import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import datetime

#Makes all the graphs that are used in makeReport for this project

plt.style.use('seaborn-v0_8')

#Fetch all stock info needed
stock = yf.Ticker("EQNR")

def makeIncomeGraph(stck):
    income_data = stck.income_stmt
    x = stck.income_stmt.columns

    plt.gca().xaxis.axis_date
    plt.ylabel('Billions of USD')
    plt.plot(x, income_data.loc['Total Revenue'] / 1000000000, linestyle='solid', label='Total Revenue', color='blue')
    plt.plot(x, income_data.loc['Normalized EBITDA'] / 1000000000, linestyle='solid', label='EBITDA', color='green')
    plt.plot(x, income_data.loc['Operating Income'] / 1000000000, linestyle='solid', label='Operating Income', color='black')
    plt.plot(x, income_data.loc['Net Income'] / 1000000000, linestyle='dashed', label='Net Income', color='black')
    plt.plot(x, income_data.loc['Total Expenses'] / 1000000000, linestyle='dashed', label='Total Expenses', color='grey')
    plt.legend(loc='best')
    plt.title('Company Performance')

    plt.show()
    print("")

def makeDebtGraph(stck):
    debt_data = stock.balance_sheet
    x = debt_data.columns

    plt.gca().xaxis.axis_date
    plt.ylabel('Billions of USD')
    plt.plot(x, debt_data.loc['Net Debt'] / 1000000000, linestyle='solid', label='Net Debt', color='blue')
    plt.plot(x, debt_data.loc['Total Debt'] / 1000000000, linestyle='solid', label='Total Debt', color='black')
    plt.legend(loc='upper right')
    plt.title('Company Debt')

    plt.show()
    print("")

def makeDividendGraph(stck):
    divi_data = stock.dividends
    #Resize the data to consist of 2 columns with each row representing one year
    divi_data_y = pd.DataFrame(divi_data.resample('YE').sum())
    divi_data_y.reset_index(inplace=True)
    divi_data_y['Year'] = divi_data_y['Date'].dt.year

    plt.gca().xaxis.axis_date
    plt.xlabel('Years')
    plt.ylabel('Dividend payed out (USD)')
    plt.bar(divi_data_y['Year'], divi_data_y['Dividends'], label='Dividends (USD)')

    plt.show()
    print("")

makeDividendGraph(stock)