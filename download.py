import yfinance as yf
import csv
import numpy as np
import pandas as pd

tickers=[
'vinex',
'vfinx'
    ]

for ticker in tickers:
    tickerTag = yf.Ticker(ticker)

    df = pd.read_csv('{}.csv'.format(ticker), index_col='Date')
    print(df.head())
    df = df.set_index(pd.DatetimeIndex(df.index, dtype='<M8[ns]'))

    new_df = yf.download(ticker, start='2021-01-01', end='2022-01-01')

    df = pd.concat([df, new_df]).sort_index()
    df = df[~df.index.duplicated(keep='first')]
    df.to_csv("{}.csv".format(ticker))
  