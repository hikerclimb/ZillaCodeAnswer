import pandas as pd
import numpy as np
import datetime
import json
import math
import re

# Define data for df1
data1 = {
    'product_id': ['P1', 'P2', 'P3'],
    'manufacturing_date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'manufacturing_location': ['Location_A', 'Location_B', 'Location_C']
}

# Create df1 (converting manufacturing_date to datetime)
df1 = pd.DataFrame(data1)
df1['manufacturing_date'] = pd.to_datetime(df1['manufacturing_date'])

# Define data for df2
data2 = {
    'product_id': ['P1', 'P2', 'P3'],
    'product_name': ['Widget_A', 'Gadget_B', 'Device_C'],
    'product_type': ['Widget', 'Gadget', 'Device']
}

# Create df2
df2 = pd.DataFrame(data2)

def etl(df1, df2):
    out = df1.merge(df2, on= "product_id", how="inner")
    out["row_number"] = np.arange(1, len(out) + 1)
    return out

print(etl(df1,df2))
