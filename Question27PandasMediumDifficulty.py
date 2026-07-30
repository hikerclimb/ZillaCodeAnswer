import pandas as pd
import numpy as np
import datetime
import json
import math
import re

# 1. Create MortgageDetails DataFrame
mortgage_details_data = {
    "MortgageID": ["M1", "M2", "M3"],
    "MortgageType": ["Fixed", "Variable", "Adjustable"],
    "InterestRate": [4.5, 3.2, 2.8],
}
df_mortgage_details = pd.DataFrame(mortgage_details_data)

# 2. Create UserMortgages DataFrame
user_mortgages_data = {
    "UserID": ["U1", "U2", "U3", "U4"],
    "MortgageID": ["M1", "M1", "M2", "M3"],
}
df_user_mortgages = pd.DataFrame(user_mortgages_data)

def etl(MortgageDetails, UserMortgages):
    merged_df = pd.merge(
        UserMortgages,
        MortgageDetails,
        on="MortgageID",
        how="inner",
    )

    result = (
        merged_df.groupby("MortgageType")
        .apply(
            lambda x: x["InterestRate"].sum()
            / x["UserID"].nunique()
        )
        .reset_index()
    )

    result.columns = [
        "MortgageType",
        "RateOfMortgage",
    ]

    return result
    

print(etl(df_mortgage_details,df_user_mortgages))
