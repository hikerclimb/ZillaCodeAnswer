
import pandas as pd
import numpy as np
import datetime
import json
import math
import re

df_sales = pd.DataFrame({
    'sales_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
    'product_id': ['P1', 'P2', 'P3', 'P4', 'P5'],
    'date': ['2023-06-01', '2023-06-02', '2023-06-02', '2023-06-01', '2023-06-03'],
    'quantity_sold': [10, 15, 20, 12, 25]
})

df_products = pd.DataFrame({
    'product_id': ['P1', 'P2', 'P3', 'P4', 'P5'],
    'product_name': ['Camping Tent', 'Hiking Shoes', 'Fishing Rod', 'Insulated Bottle', 'Outdoor Grill'],
    'product_category': ['Camping', 'Hiking', 'Fishing', 'Hiking', 'Camping']
})

df_combined = pd.merge(df_sales, df_products, on='product_id', how='inner')
df_summary = df_combined.groupby(['date','product_category'])['quantity_sold'].sum().reset_index(name="total_quantity")
return df_summary
