import pandas as pd
import numpy as np
import datetime
import json
import math
import re

artifacts = pd.DataFrame(
    {
        "ID": [1, 2, 3],
        "Item": ["Pottery", "Weapon", "Jewel"],
        "Period": ["Prehistoric", "Medieval", "Roman"],
        "Material": ["clay", "metal", "gold"],
        "Quantity": [150, 90, 200],
    }
)

def etl(artifacts):
    artifacts['Material'] = artifacts['Material'].str.upper()
    artifacts.query('Quantity > 100', inplace= True)
    return artifacts

print(etl(artifacts))
