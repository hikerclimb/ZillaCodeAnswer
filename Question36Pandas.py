import pandas as pd
import numpy as np
import datetime
import json
import math
import re

venture_capitalist_df = pd.DataFrame({
    'vc_id': ['VC1', 'VC2', 'VC3', 'VC4'],
    'vc_name': ['VC Firm 1', 'VC Firm 2', 'VC Firm 3', 'VC Firm 4'],
    'funding_limit': [1.5, 2.0, 1.75, 2.5]
})

funded_startups_df = pd.DataFrame({
    'startup_id': ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8'],
    'startup_name': ['Startup 1', 'Startup 2', 'Startup 3', 'Startup 4', 'Startup 5', 'Startup 6', 'Startup 7', 'Startup 8'],
    'vc_id': ['VC1', 'VC1', 'VC2', 'VC2', 'VC3', 'VC3', 'VC4', 'VC4'],
    'funding': [2.0, 1.0, 2.5, 2.0, 1.8, 1.7, 3.0, 2.0]
})

def etl(venture_capitalist_df, funded_startups_df):
    df_combined = pd.merge(funded_startups_df, venture_capitalist_df, on='vc_id', how='inner')
    average = df_combined.groupby(['vc_id'])['funding'].mean().reset_index(name = 'avg_funding')
    funding_limit = df_combined.groupby(['vc_id'])['funding_limit'].mean().reset_index(name = 'funding_limit')
    if ((average['avg_funding'] > funding_limit['funding_limit']).any()):
        greaterthan = average['avg_funding'] > funding_limit['funding_limit']
        almostout = pd.merge(average[greaterthan], funding_limit[greaterthan], on="vc_id", how="inner")
        out = pd.merge(almostout, venture_capitalist_df, on = "vc_id", how= "inner")
        out.rename(columns={"funding_limit_x": "funding_limit"}, inplace=True)
        out.drop(columns='funding_limit_y', inplace = True)
        return out
print(etl(venture_capitalist_df, funded_startups_df))
