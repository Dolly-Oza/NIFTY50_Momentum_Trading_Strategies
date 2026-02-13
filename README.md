# NIFTY50_Momentum_Trading_Strategies

**About This Project**

This project tests a simple momentum investing strategy using stocks from the Nifty 50 index.

The idea behind momentum is:

Stocks that performed well in the past 12 months may continue to perform well in the near future.

The strategy selects the top 5 best-performing stocks each month and holds them for the next month.

**What the Code Does**

Downloads historical price data of Nifty 50 stocks using yfinance

Calculates daily returns

Converts them into monthly returns

Calculates 12-month past returns for each stock

Every month:

Selects the top 5 stocks based on 12-month performance

Forms an equal-weight portfolio

Holds for 1 month

Repeats this process until the latest date

Compares performance with NIFTY index (Buy & Hold)

**Results**

Momentum Strategy CAGR: 19.18%

NIFTY Buy & Hold CAGR: 13.67%

The momentum strategy performed better than simply holding the index during this period.

**Data Used**

Stocks: Nifty 50 companies

Data source: Yahoo Finance

Time period: From 2012 onwards

**Assumptions**

No transaction costs

Equal investment in top 5 stocks

Monthly rebalancing

Static list of Nifty 50 stocks

**Libraries Used**

Python

pandas

numpy

yfinance

**How to Run**
pip install yfinance pandas numpy
python momentum_strategy.py
