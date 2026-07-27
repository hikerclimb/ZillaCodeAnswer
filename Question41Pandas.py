import pandas as pd
import numpy as np
import datetime
import json
import math
import re

data = {
    "id": [1, 2, 3, 4, 5],
    "name": [
        "One World Trade Center",
        "Willis Tower",
        "Burj Khalifa",
        "The Shard",
        "Abraj Al-Bait Clock Tower",
    ],
    "city": ["New York", "Chicago", "Dubai", "London", "Mecca"],
    "country": ["USA", "USA", "UAE", "UK", "Saudi Arabia"],
    "height_m": [541.3, 442.1, 828.0, 309.6, 601.0],
    "floors": [104, 108, 163, 72, 120],
}

# Create DataFrame
buildings = pd.DataFrame(data)

def etl(buildings):
    buildings['avg_height_per_floor']= np.where(buildings['floors'] > 0, buildings['height_m']/buildings['floors'], 0)
    buildings = buildings.drop(columns=['floors', 'height_m'])
    return buildings.round(2)

print(etl(buildings))
