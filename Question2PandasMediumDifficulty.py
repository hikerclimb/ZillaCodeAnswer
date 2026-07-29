import pandas as pd
import numpy as np
import datetime
import json
import math
import re


# 1. Customers DataFrame
customers_data = {
    "customer_id": [1, 2],
    "first_name": ["John", "Jane"],
    "last_name": ["Doe", "Smith"],
    "email": ["john.doe@email.com", "jane.smith@email.com"],
}
df_customers = pd.DataFrame(customers_data)

# 2. Orders DataFrame
orders_data = {
    "order_id": [1001, 1002],
    "customer_id": [1, 2],
    "product_id": [101, 102],
    "order_date": ["2023-01-10", "2023-01-11"],
}
df_orders = pd.DataFrame(orders_data)
# Convert order_date string column to proper datetime format
df_orders["order_date"] = pd.to_datetime(df_orders["order_date"])

# 3. Products DataFrame
products_data = {
    "product_id": [101, 102],
    "product_name": ["Product A", "Product B"],
    "category": ["Category1", "Category2"],
}
df_products = pd.DataFrame(products_data)

def etl(customers, orders, products):
    merge1 = pd.merge(customers, orders, on= "customer_id", how="inner")
    merge1['customer_name'] = merge1['first_name'] +' ' + merge1['last_name']
    out = pd.merge(merge1, products, on= "product_id", how="inner")
    return out[['category', 'customer_name', 'email', 'order_date', 'order_id', 'product_name']]

print(etl(df_customers, df_orders, df_products))
