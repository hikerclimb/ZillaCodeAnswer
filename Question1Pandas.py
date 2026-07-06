import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(input_df):
	current_year = 2024
    filtered_df = input_df[
        (input_df["view_count"] > 1000000)
        & (
            input_df["release_year"]
            >= current_year - 5
        )
    ]
    return filtered_df