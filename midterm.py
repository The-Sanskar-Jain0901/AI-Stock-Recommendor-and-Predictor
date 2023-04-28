import yfinance as yf
import datetime
import pandas as pd
import pivots as pv
import adx as adx

# pv.pivots()
stock_data = pd.read_csv('aicp.csv')
stock_data['weights'] = 0
for tickerSymbol in stock_data['Symbol']:
    start_date = datetime.datetime.now() - datetime.timedelta(days=365)
    end_date = datetime.datetime.now()
    stock = yf.download(tickerSymbol + '.NS', start=start_date,
                        end=end_date, interval='1d')
    adx_val = adx.adx(stock)
    stock_data.loc[str(tickerSymbol) == stock_data['Symbol'],
                   'weights'] += adx_val
    if adx_val == 1:
        rded = stock_data.loc[str(tickerSymbol) ==
                              stock_data['Symbol'], 'R1.5']
        r1 = stock_data.loc[str(tickerSymbol) ==
                            stock_data['Symbol'], 'R1']
        rsava = stock_data.loc[str(tickerSymbol) ==
                               stock_data['Symbol'], 'R1.25']
        if stock['Close'][len(stock)-1] > rded.iloc[0]:
            stock_data.loc[str(tickerSymbol) == stock_data['Symbol'],
                           'weights'] += 0
        elif stock['Close'][len(stock)-1] > r1.iloc[0]:
            stock_data.loc[str(tickerSymbol) == stock_data['Symbol'],
                           'weights'] += 3
        elif stock['Close'][len(stock)-1] > (r1.iloc[0]-abs(r1.iloc[0]-rsava.iloc[0])):
            stock_data.loc[str(tickerSymbol) == stock_data['Symbol'],
                           'weights'] += 4
        elif stock['Close'][len(stock)-1] > (r1.iloc[0]-abs(r1.iloc[0]-rded.iloc[0])):
            stock_data.loc[str(tickerSymbol) == stock_data['Symbol'],
                           'weights'] += 2
        else:
            stock_data.loc[str(tickerSymbol) == stock_data['Symbol'],
                           'weights'] += 1
print(stock_data)
