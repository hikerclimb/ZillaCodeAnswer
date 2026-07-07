import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(products_df, orders_df):
	# Join the two DataFrames on the product_id column
    joined_df = products_df.merge(
        orders_df, on="product_id", how="inner"
    )

    # Calculate the total_orders_count for each category
    total_orders_count = (
        joined_df.groupby("category")["order_id"]
        .count()
        .reset_index()
        .rename(
            columns={
                "order_id": "total_orders_count"
            }
        )
    )

    # Calculate the average price for each category
    avg_price = (
        joined_df.groupby("category")["price"]
        .mean()
        .reset_index()
        .rename(columns={"price": "avg_price"})
    )

    # Join the two aggregated DataFrames on the category column
    result_df = total_orders_count.merge(
        avg_price, on="category", how="inner"
    )

    return result_df
