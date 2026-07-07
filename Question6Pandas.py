import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(social_media):
    social_media["text"] =social_media["text"].replace(r"\bPython\b", "PySpark", regex = True)
    return social_media
