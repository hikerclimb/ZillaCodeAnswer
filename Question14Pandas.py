
import pandas as pd
import numpy as np
import datetime
import json
import math
import re
import io
#1. Create pe_firms DataFrame
# 1. Base pe_firms Data
pe_firms_csv = """
firm_id,firm_name,founded_year,location
1,ABC Fund,2010,New York
2,XYZ Fund,2005,London
3,DEF Fund,2015,Paris
4,GHI Fund,2018,Hong Kong
5,JKL Fund,2009,Sydney
6,MNO Fund,2012,Tokyo
7,PQR Fund,2017,Mumbai
8,STU Fund,2003,Frankfurt
9,VWX Fund,2011,Berlin
10,YZA Fund,2006,Toronto
"""
pe_firms = pd.read_csv(io.StringIO(pe_firms_csv.strip()))

# 2. Base pe_funds Data
pe_funds_csv = """
fund_id,firm_id,fund_name,fund_size,fund_start_year,fund_end_year
101,1,ABC I,100,2010,2015
102,1,ABC II,150,2015,2020
103,2,XYZ I,200,2010,2018
104,3,DEF I,80,2017,2022
105,3,DEF II,120,2020,2025
106,4,GHI I,90,2019,2024
107,5,JKL I,60,2010,2015
108,5,JKL II,70,2015,2020
109,6,MNO I,110,2013,2018
110,7,PQR I,40,2018,2023
"""
pe_funds = pd.read_csv(io.StringIO(pe_funds_csv.strip()))

# 3. Base pe_investments Data (Dropping the NaN row to avoid float conversion)
pe_investments_csv = """
investment_id,fund_id,company_name,investment_amount,investment_date
1001,101,Company A,10,2012-05-15
1002,101,Company B,20,2013-06-20
1003,102,Company C,30,2016-07-25
1004,103,Company D,15,2017-03-18
1005,104,Company E,8,2019-09-05
1006,105,Company F,25,2021-01-12
1007,105,Company G,12,2022-02-28
"""
pe_investments = pd.read_csv(io.StringIO(pe_investments_csv.strip()))



# 2. Merge pe_investments with pe_funds on 'fund_id'
# Then merge the result with pe_firms on 'firm_id'
def etl(pe_firms, pe_funds, pe_investments):
	merged_df = pe_investments.merge(pe_funds, on='fund_id', how='outer').merge(pe_firms, on='firm_id', how='outer').dropna(how='all')
    return merged_df

    print(merged_df)
    merged_df.to_csv('merged_output.csv', index=False)

