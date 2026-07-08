import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(calls_df, customers_df):
    # Join calls_df and customers_df on cust_id column
    joined_df = calls_df.merge(
        customers_df, on="cust_id"
    )

    # Aggregate the joined DataFrame by date
    agg_df = joined_df.groupby("date").agg(
        num_customers=("cust_id", "nunique"),
        total_duration=("duration", "sum"),
    )

    return agg_df.reset_index()
