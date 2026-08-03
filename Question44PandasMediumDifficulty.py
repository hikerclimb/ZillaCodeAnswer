import pandas as pd
import numpy as np
import datetime
import json
import math
import re

# 1. Portfolio DataFrame
portfolio_data = {
    "PE_firm": ["Alpha", "Alpha", "Beta", "Beta", "Gamma", "Gamma"],
    "company": ["A", "B", "A", "C", "B", "C"],
    "shares": [1000, 2000, 1500, 2500, 1200, 1300],
}
df_portfolio = pd.DataFrame(portfolio_data)

# 2. Prices DataFrame
prices_data = {
    "date": [
        "2023-01-01",
        "2023-01-01",
        "2023-01-01",
        "2023-01-02",
        "2023-01-02",
        "2023-01-02",
    ],
    "company": ["A", "B", "C", "A", "B", "C"],
    "closing_price": [50.0, 20.0, 30.0, 52.0, 21.0, 31.0],
}
df_prices = pd.DataFrame(prices_data)

# Convert date column to datetime data type
df_prices["date"] = pd.to_datetime(df_prices["date"])

def etl(portfolio, prices):
    merged_data = portfolio.merge(prices, on="company", how="inner")
    merged_data['total'] = merged_data['shares'] *  merged_data['closing_price']
    out = merged_data.groupby(['PE_firm','date'])['total'].sum().reset_index()
    out.rename(
        columns={"total": "portfolio_value"},
        inplace=True,
    )
    return out

print(etl(df_portfolio,df_prices))
