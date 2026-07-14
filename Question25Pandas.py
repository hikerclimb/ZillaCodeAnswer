import pandas as pd
import numpy as np
import datetime
import json
import math
import re

mines_data = {
    'id': [1, 2, 3],
    'name': ['Mine Alpha', 'Mine Beta', 'Mine Gamma'],
    'location': ['Australia', 'Canada', 'South Africa']
}
mines = pd.DataFrame(mines_data)

extraction_data = {
    'mine_id': [1, 2, 3, 1, 2, 3],
    'date': ['2023-06-30', '2023-06-30', '2023-06-30', '2023-06-29', '2023-06-29', '2023-06-29'],
    'mineral': ['Gold', 'Silver', 'Diamond', 'Gold', 'Silver', 'Diamond'],
    'quantity': [1000.0, 1200.0, 800.0, 900.0, 1300.0, 750.0]
}
extraction = pd.DataFrame(extraction_data)

def etl(mines, extraction):
    merged_df = pd.merge(extraction, mines, left_on='mine_id', right_on='id').drop(columns=['id']).groupby(['mineral', 'location'])['quantity'].sum()
    df = merged_df.to_frame().reset_index()
    result_df= df.rename(columns = {'quantity': 'total_quantity'})
    out = result_df.sort_values(by=['location', 'mineral'],ascending=[True,True])
    return out
etl()
