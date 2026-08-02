import pandas as pd
import numpy as np
import datetime
import json
import math
import re

# Define data for df_orders
orders_data = {
    'order_id': [1, 2, 3, 4, 5],
    'product_id': ['P001', 'P002', 'P001', 'P003', 'P004'],
    'user_id': ['U001', 'U001', 'U002', 'U002', 'U003'],
    'order_date': ['02/25/2023', '03/14/2023', '03/16/2023', '03/18/2023', '04/01/2023']
}

# Create df_orders and parse dates
df_orders = pd.DataFrame(orders_data)
df_orders['order_date'] = pd.to_datetime(df_orders['order_date'])

# Define data for df_products
products_data = {
    'product_id': ['P001', 'P002', 'P003', 'P004'],
    'product_name': ['Product 1', 'Product 2', 'Product 3', 'Product 4'],
    'category': ['Electronics', 'Clothing', 'Home Goods', 'Books']
}

# Create df_products
df_products = pd.DataFrame(products_data)

def etl(df_orders, df_products):
    out = df_orders.merge(df_products, on="product_id", how="inner")
    df_orders["order_date"] = pd.to_datetime(df_orders["order_date"])
    out["is_weekend"] = df_orders["order_date"].dt.weekday >=5
    return out[['category', 'is_weekend', 'order_date', 'product_name', 'user_id']]

print(etl(df_orders, df_products))
