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

def calc_1500m_target(target_time_2000m):
    distance = 1500
    distance_factor = 0.475
    sets = 5

    single_distance_conversion = distance * (1 + (sets - 1) * distance_factor)

    result = (target_time_2000m * (2000 / single_distance_conversion)/((2000/single_distance_conversion)**(19/18))) / 4

    return result

def theoretical_pace(pace, rate, target_rate=34, calibration = 1):
    return pace/(target_rate/rate)**(calibration*(1/3))

x_rate_list = np.arange(16, 42, 2)
list = []
calibration = 0.88
space = 1.35 * 2
for i, rate in enumerate(x_rate_list):
    pace = theoretical_pace(92, 37, rate, calibration)
    dps = (60 * 500 / pace) / rate
    babble_space = (dps - space * 3) / space
    list.append({
        "SR": rate,
        "/500m":  sec_to_time(pace),
        "DPS": dps,
        "泡空き": babble_space
    })
df = pd.DataFrame(list)

rate = 36
pace = 97

dps = (60 * 500 / pace) / rate

babble_space = (dps - space * 3) / space

print(dps)
print(babble_space)
df