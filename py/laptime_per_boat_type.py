import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import optimize
from statistics import median

def sec_to_time(time):
    m = math.floor(time / 60)
    s = round((time % 60), 1)
    if s < 10:
        return str(m) + ':0' + str(s)
    return str(m) + ':' + str(s)

pace_list = np.arange(90, 130, 1)
list = []
for pace in pace_list:
    list.append({
        "m1x": sec_to_time(1.107 * pace),
        "m2+": sec_to_time(1.141 * pace),
        "m2-": sec_to_time(1.08  * pace),
        "m2x": sec_to_time(1.018 * pace),
        "m4+": sec_to_time(1     * pace),
        "m4-": sec_to_time(0.961 * pace),
        "m4x": sec_to_time(0.933 * pace),
        "m8+": sec_to_time(0.899 * pace),
        "w1x": sec_to_time(1.245 * pace),
        "w2-": sec_to_time(1.202 * pace),
        "w2x": sec_to_time(1.133 * pace),
        "w4x+":sec_to_time(1.076 * pace),
        "w4x": sec_to_time(1.048 * pace),
        "w4+": sec_to_time(1.115 * pace),
    })

df = pd.DataFrame(list)

df.to_csv('./../dst/lap_time_per_boat_type.csv')

df