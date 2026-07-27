import pandas as pd
import numpy as np
import datetime
import json
import math
import re
transactions_data = {
    'trans_id': [1, 2, 3],
    'trans_amt': [500.0, 200.0, 300.0],
    'date': ['2023-07-01', '2023-07-02', '2023-07-03'],
    'cust_id': [1001, 1002, 1003]
    }

transactions = pd.DataFrame(transactions_data)
    # Convert the 'date' column to datetime format
    #transactions['date'] = pd.to_datetime(transactions['date'])    
    # 2. Create customers DataFrame
customers_data = {
    'cust_id': [1001, 1002, 1003],
    'first_name': ['John', 'Jane', 'Bob'],
    'last_name': ['Doe', 'Smith', 'Johnson'],
        'age': [30, 40, 50]
}
        
customers = pd.DataFrame(customers_data)
    
def etl(transactions, customers):
    cross_joined = pd.merge(transactions, customers, how='cross')
    output = cross_joined.drop(columns=["cust_id_x"])
    out = output.rename(columns={"cust_id_y": "cust_id"})
    #output = out[['age','cust_id', 'date', 'first_name', 'last_name', 'trans_amt', 'trans_id']]
    return out

print(etl(transactions, customers))
