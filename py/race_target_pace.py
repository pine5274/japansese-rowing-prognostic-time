import pandas as pd
import numpy as np
import math

def sec_to_time(time):
    m = math.floor(time / 60)
    s = round((time % 60), 1)
    if s < 10:
        return str(m) + ':0' + str(s)
    return str(m) + ':' + str(s)

df = pd.read_csv('./../dst/trends/PT_time.csv', sep=',')
print(df)