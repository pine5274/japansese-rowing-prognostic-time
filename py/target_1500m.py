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

print(sec_to_time(calc_1500m_target(420)))

list = []

target = np.arange(360, 510, 1)

for x in target:
    list.append({"2000m": sec_to_time(x),"2000m ave": sec_to_time(x/4), "1500m *5 ave": sec_to_time(calc_1500m_target(x)), "diff": sec_to_time(calc_1500m_target(x)- x/4)})

df = pd.DataFrame(list)

df.to_csv('./../dst/1500m_target_ave.csv')