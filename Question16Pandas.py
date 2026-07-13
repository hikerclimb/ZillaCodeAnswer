import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(employees, payroll):
    joined_result = employees.merge(payroll, on="employee_id", how="inner")
    pay = np.where(joined_result.hours_worked <= 40, joined_result.hours_worked * joined_result.hourly_rate, 
    (40 * joined_result.hourly_rate) + (1.5* (joined_result.hours_worked - 40) * 
    joined_result.hourly_rate))
    joined_result["pay"] = pay
    result = joined_result.drop(columns = ["age", "hours_worked", "hourly_rate"], axis= 1)
    return result
