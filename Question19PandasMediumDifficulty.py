import pandas as pd
import numpy as np
import datetime
import json
import math
import re

# 1. Companies DataFrame
companies_data = {
    "company_id": [1, 2, 3, 4, 5],
    "company_name": [
        "AlphaTech",
        "BetaHealth",
        "GammaEntertainment",
        "DeltaGreen",
        "EpsilonFinance",
    ],
    "industry": [
        "Technology",
        "Healthcare",
        "Entertainment",
        "Renewable Energy",
        "Finance",
    ],
}
companies_df = pd.DataFrame(companies_data)

# 2. Investments DataFrame
investments_data = {
    "investment_id": [1, 2, 3, 4, 5],
    "company_id": [1, 2, 3, 4, 5],
    "amount": [5000000, 3000000, 1000000, 4000000, 2000000],
}
investments_df = pd.DataFrame(investments_data)

def etl(companies, investments):
    merged_data = pd.merge(companies, investments, on="company_id", how="inner")
    grouped_data = merged_data.groupby('industry')[['industry', 'amount']].sum()
    renamed_column = grouped_data.rename(columns={'amount': 'total_investment'})
    sorted_data = renamed_column.sort_values(by="total_investment", ascending=False)
    return sorted_data
print(etl(companies_df,investments_df))
