import pandas as pd
import numpy as np
import datetime
import json
import math
import re

# 1. Products DataFrame
products_data = {
    "product_id": [1, 2, 3, 4, 5],
    "name": ["Apple Juice", "Orange Juice", "Chocolate Bar", "Potato Chips", "Fresh Strawberries"],
    "category": ["Beverages", "Beverages", "Snacks", "Snacks", "Fruits"]
}
df_products = pd.DataFrame(products_data)

# 2. Sales DataFrame
sales_data = {
    "sale_id": [1, 2, 3, 4, 5],
    "product_id": [1, 1, 2, 3, 4],
    "quantity": [10, 5, 8, 2, 15],
    "revenue": [20.0, 10.0, 16.0, 4.0, 30.0]
}
df_sales = pd.DataFrame(sales_data)

# 3. Inventory DataFrame
inventory_data = {
    "product_id": [1, 2, 3, 4, 5],
    "stock": [50, 40, 30, 20, 10],
    "warehouse": ["Warehouse1"] * 5
}
df_inventory = pd.DataFrame(inventory_data)

def etl(products, sales, inventory):
    merged1 = pd.merge(products, sales, on="product_id", how="outer")
    total_quantity = merged1.groupby(['name', 'product_id'])['quantity'].transform('sum')
    merged1['total_quantity'] = total_quantity
    total_revenue = merged1.groupby(['name','product_id'])['revenue'].transform('sum')
    merged1['total_revenue'] = total_revenue
    merged1.drop_duplicates('name' ,inplace=True)
    merged2 = pd.merge(merged1, inventory, on="product_id", how="outer")
    total_stock = merged2.groupby('product_id')['stock'].transform('sum')
    merged2['total_stock'] = total_stock
    return merged2[['category', 'name', 'product_id', 'total_quantity', 'total_revenue', 'total_stock']]

print(etl(df_products, df_sales, df_inventory))
