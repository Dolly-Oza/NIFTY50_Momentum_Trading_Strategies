import nselib as nse
import yfinance as yf
import numpy as np
import pandas as pd

def get_nifty50_symbols():
    """Returns a list of Yahoo Finance symbols for Nifty 50 stocks."""
    symbols = [
        'RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'INFY.NS', 'ICICIBANK.NS',
        'HINDUNILVR.NS', 'ITC.NS', 'SBIN.NS', 'BHARTIARTL.NS', 'KOTAKBANK.NS',
        'BAJFINANCE.NS', 'LT.NS', 'HCLTECH.NS', 'AXISBANK.NS', 'ASIANPAINT.NS',
        'MARUTI.NS', 'SUNPHARMA.NS', 'TITAN.NS', 'WIPRO.NS', 'ULTRACEMCO.NS',
        'ONGC.NS', 'NTPC.NS', 'JSWSTEEL.NS', 'POWERGRID.NS', 'M&M.NS',
        'BAJAJFINSV.NS', 'HINDALCO.NS', 'GRASIM.NS', 'TATAMOTORS.NS', 'TATASTEEL.NS',
        'DIVISLAB.NS', 'NESTLEIND.NS', 'INDUSINDBK.NS', 'ADANIPORTS.NS', 'TECHM.NS',
        'BPCL.NS', 'COALINDIA.NS', 'DRREDDY.NS', 'BRITANNIA.NS', 'EICHERMOT.NS',
        'SHREECEM.NS', 'HEROMOTOCO.NS', 'SBILIFE.NS', 'IOC.NS', 'UPL.NS',
        'BAJAJ-AUTO.NS', 'TATACONSUM.NS', 'HDFCLIFE.NS', 'CIPLA.NS', 'APOLLOHOSP.NS'
    ]
    return symbols

stocks = get_nifty50_symbols()
print(f"Downloading data for {len(stocks)} Nifty 50 stocks...")


df = yf.download(stocks, start="2012-01-01")["Close"]
ret_df = df.pct_change()
print(ret_df)
mtl_ret = (ret_df + 1).resample("M").prod()
print(mtl_ret)
mtl_12 = mtl_ret.rolling(12).apply(np.prod).dropna()
print(mtl_12)
top_ = mtl_12.loc["2012-12-31"].nlargest(5)
print(top_)
print(top_.name)
print(mtl_ret[top_.name:][1:2])
relevant_ret = mtl_ret[top_.name:][1:2][top_.index]
print(relevant_ret)
print(relevant_ret.mean(axis=1))

def top_performers(date):
    all_ = mtl_12.loc[date]
    top = all_.nlargest(5)
    relevant_ret = mtl_ret[top.name:][1:2][top.index]
    return (relevant_ret).mean(axis=1).values[0]

print(top_performers("2012-12-31"))
mom_ret = []
for date in mtl_12.index[:-1]:
    mom_ret.append(top_performers(date))
mom_series = pd.Series(
    mom_ret,
    index=mtl_12.index[:-1]
)

print(mom_series)
print(mom_series.prod())

nifty = yf.download("^NSEI", start="2012-01-01")["Close"]
print((nifty.pct_change() + 1).prod())

years = (mom_series.index[-1] - mom_series.index[0]).days / 365.25

strategy_cagr = (pd.Series(mom_ret).prod()) ** (1 / years) - 1
nifty_cagr = float((nifty.pct_change() + 1).prod()) ** (1 / years) - 1

print(f"Momentum Strategy CAGR: {strategy_cagr * 100:.2f}%")
print(f"NIFTY Buy & Hold CAGR: {nifty_cagr * 100:.2f}%")