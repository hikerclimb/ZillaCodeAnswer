
import pandas as pd
import numpy as np
import datetime
import json
import math
import re

df_temperature = pd.DataFrame(
    {"ExperimentID": [1.0, 2.0, 3.0], "Temperature": [273.15, 293.15, 313.15]}
)

# Create df_pressure
df_pressure = pd.DataFrame(
    {"ExperimentID": [1.0, 3.0, 4.0], "Pressure": [1.0, 2.0, 1.5]}
)



def etl(df_temperature, df_pressure):
    merged_data = pd.merge(df_pressure, df_temperature, on="ExperimentID", how = "inner")
    merged_data["Result"] = merged_data["Temperature"] * merged_data["Pressure"]
    return merged_data[["ExperimentID", "Result"]]
print(etl(df_temperature, df_pressure))
