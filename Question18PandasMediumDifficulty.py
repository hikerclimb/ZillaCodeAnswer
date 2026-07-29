import pandas as pd
import numpy as np
import datetime
import json
import math
import re

# 1. Products DataFrame
products_data = {
    'ProductID': [1, 2, 3, 4, 1],
    'ProductName': ['Widget A', 'Widget B', 'Widget C', 'Widget D', 'Widget A'],
    'Category': ['Type1', 'Type1', 'Type2', 'Type2', 'Type1']
}
products_df = pd.DataFrame(products_data)

# 2. Manufacturing Processes DataFrame
manufacturing_data = {
    'ProcessID': [1001, 1002, 1003, 1004, 1005],
    'ProductID': [1, 2, 3, 4, 1],
    'ProcessName': ['Cutting', 'Cutting', 'Cutting', 'Cutting', 'Shaping'],
    'Duration': [1.5, 1.6, 1.8, 1.5, 2.0]
}
manufacturing_processes_df = pd.DataFrame(manufacturing_data)

def etl(products_df, manufacturing_processes_df):
    return pd.merge(products_df, manufacturing_processes_df, on="ProductID", how="inner").drop_duplicates()

print(etl(products_df, manufacturing_processes_df))
