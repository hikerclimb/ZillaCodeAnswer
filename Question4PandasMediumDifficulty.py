import pandas as pd
import numpy as np
import datetime
import json
import math
import re

data = {
    "user_id": [1, 2, 3, 4, 5],
    "email": [
        "alice@example.com",
        "bob@domain.net",
        "carol@email.org",
        "dave@site.com",
        "eve@platform.io",
    ],
    # Phone numbers are kept as strings to preserve formatting/leading zeroes
    "phone": [
        "5551234567",
        "5559876543",
        "5551239876",
        "5554567890",
        "5559871234",
    ],
}

input_df = pd.DataFrame(data)
def etl(input_df):
    input_df['email_domain'] = input_df['email'].str.replace(r'^.*@', '', regex=True)
    input_df['anon_phone'] = input_df['phone'].astype(str).str.replace(r'^\d{6}', '******', regex=True)
    return input_df[['anon_phone', 'email_domain', 'user_id']]

print(etl(input_df))
