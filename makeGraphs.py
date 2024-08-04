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
    
    fig, ax = plt.subplots()

    plt.gca().xaxis.axis_date
    plt.ylabel('Billions of USD')
    ax.plot(x, income_data.loc['Total Revenue'] / 1000000000, linestyle='solid', label='Total Revenue', color='blue')
    ax.plot(x, income_data.loc['Normalized EBITDA'] / 1000000000, linestyle='solid', label='EBITDA', color='green')
    ax.plot(x, income_data.loc['Operating Income'] / 1000000000, linestyle='solid', label='Operating Income', color='black')
    ax.plot(x, income_data.loc['Net Income'] / 1000000000, linestyle='dashed', label='Net Income', color='black')
    ax.plot(x, income_data.loc['Total Expenses'] / 1000000000, linestyle='dashed', label='Total Expenses', color='grey')
    ax.legend(loc='best')
    ax.set_title('Company Performance')

    return fig

def makeDebtGraph(stck):
    debt_data = stock.balance_sheet
    x = debt_data.columns
    
    fig, ax = plt.subplots()

    plt.gca().xaxis.axis_date
    plt.ylabel('Billions of USD')
    ax.plot(x, debt_data.loc['Net Debt'] / 1000000000, linestyle='solid', label='Net Debt', color='blue')
    ax.plot(x, debt_data.loc['Total Debt'] / 1000000000, linestyle='solid', label='Total Debt', color='black')
    ax.legend(loc='upper right')
    ax.set_title('Company Debt')

    return fig

def makeDividendGraph(stck):
    
    divi_data = stock.dividends
    #Resize the data to consist of 2 columns with each row representing one year
    divi_data_y = pd.DataFrame(divi_data.resample('YE').sum())
    divi_data_y.reset_index(inplace=True)
    divi_data_y['Year'] = divi_data_y['Date'].dt.year

    fig, ax = plt.subplots()

    plt.gca().xaxis.axis_date
    plt.xlabel('Years')
    plt.ylabel('Dividend payed out (USD)')
    ax.bar(divi_data_y['Year'], divi_data_y['Dividends'], label='Dividends (USD)')

    return fig