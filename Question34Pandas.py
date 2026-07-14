import pandas as pd
import numpy as np
import datetime
import json
import math
import re

page_visits = pd.DataFrame({
    'user_id': ['U1', 'U2', 'U3'],
    'page_id': ['P1', 'P3', 'P2'],
    'visit_time': ['2023-01-01 12:00:00', '2023-01-02 15:30:00', '2023-01-03 10:45:00']
})

page_likes = pd.DataFrame({
    'user_id': ['U1', 'U2', 'U3'],
    'page_id': ['P2', 'P1', 'P3'],
    'like_time': ['2023-01-02 14:20:00', '2023-01-03 16:40:00', '2023-01-04 18:55:00']
})

page_comments = pd.DataFrame({
    'user_id': ['U1', 'U2', 'U3'],
    'page_id': ['P3', 'P1', 'P2'],
    'comment_time': ['2023-01-03 13:00:00', '2023-01-04 17:10:00', '2023-01-05 19:25:00']
})

def etl():
    merged_df = [page_visits, page_likes,page_comments]
    final_df = pd.concat(merged_df, ignore_index=True)
    for i in range(0,len(final_df)):
        if pd.notna(final_df['visit_time'].iloc[i]) and final_df['like_time'].isna().any() and final_df['comment_time'].isna().any():
            final_df.at[i, 'interaction_type'] = 'visit'
        elif pd.notna(final_df['like_time'].iloc[i]) and final_df['visit_time'].isna().any() and final_df['comment_time'].isna().any():
            final_df.at[i, 'interaction_type'] = 'like'
        elif pd.notna(final_df['comment_time'].iloc[i]) and final_df['like_time'].isna().any() and final_df['visit_time'].isna().any():
            final_df.at[i, 'interaction_type'] = 'comment'
            
        if pd.notna(final_df['visit_time'].iloc[i]) and final_df['like_time'].isna().any() and final_df['comment_time'].isna().any():
            final_df.at[i, 'interaction_time'] = final_df['visit_time'].iloc[i]
        elif pd.notna(final_df['like_time'].iloc[i]) and final_df['visit_time'].isna().any() and final_df['comment_time'].isna().any():
            final_df.at[i, 'interaction_time'] = final_df['like_time'].iloc[i]
        elif pd.notna(final_df['comment_time'].iloc[i]) and final_df['like_time'].isna().any() and final_df['visit_time'].isna().any():
            final_df.at[i, 'interaction_time'] = final_df['comment_time'].iloc[i]
    return final_df[['interaction_time', 'interaction_type', 'page_id', 'user_id']]

print(etl())
