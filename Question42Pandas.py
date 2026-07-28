import pandas as pd
import numpy as np
import datetime
import json
import math
import re

animal_data = {
    'ID': ['A1', 'A2', 'A3', 'A4', 'A5'],
    'Species': ['Lion', 'Tiger', 'Bear', 'Lion', 'Tiger'],
    'Age': [10, 5, 7, 12, 6],
    'Weight': [200.5, 150.3, 180.2, 205.7, 155.1],
    'Region': ['Africa', 'Asia', 'North America', 'Africa', 'Asia']
}

region_data = {
    'Region': ['Africa', 'Asia', 'North America'],
    'Climate': ['Hot', 'Temperate', 'Cold']
}

df_animal = pd.DataFrame(animal_data)
df_region = pd.DataFrame(region_data)

def etl(AnimalData, RegionData):
    merged_df = pd.merge(AnimalData, RegionData, on="Region" )
    aver = pd.DataFrame()
    AverageAnimalData = merged_df.groupby(['Species', 'Climate']).agg(AvgAge=("Age", "mean"),
        AvgWeight=("Weight", "mean"), TotalAnimals= ("ID", "count")).reset_index()
    AverageAnimalData[
        "AvgWeight"
    ] = AverageAnimalData["AvgWeight"].astype(int)
    return AverageAnimalData

print(etl(df_animal, df_region))
