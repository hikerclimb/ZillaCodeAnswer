import pandas as pd
import numpy as np
import datetime
import json
import math
import re

data = {
    "interaction_id": [1, 2, 3, 4, 5],
    "user1_id": [1001, 1002, 1003, 1004, 1005],
    "user2_id": [2002, 1002, 2003, 1004, 2005],
    "interaction_type": ["like", "comment", "share", "like", "comment"],
    "timestamp": [
        "2023-01-01 10:00:00",
        "2023-01-01 11:00:00",
        "2023-01-02 10:00:00",
        "2023-01-02 11:00:00",
        "2023-01-03 10:00:00",
    ],
}

input_df = pd.DataFrame(data)

def etl(input_df):
    userId = input_df.query("user1_id == user2_id")
    counts_df = userId['user1_id'].value_counts().reset_index()
    counts_df.rename(columns={'count': 'self_interaction_count'}, inplace=True)
    return counts_df


print(etl(input_df))
