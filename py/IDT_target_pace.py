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
calibration = 0.7
for i, rate in enumerate(x_rate_list):
    list.append({
        "SR": rate,
        "m1x":  sec_to_time(theoretical_pace(434.6/4, 32, rate, calibration)),
        "m2-":  sec_to_time(theoretical_pace(423.9/4, 33, rate, calibration)),
        "m4+":  sec_to_time(theoretical_pace(392.5/4, 34, rate, calibration)),
        "m4-":  sec_to_time(theoretical_pace(377.2/4, 35, rate, calibration)),
        "m4x":  sec_to_time(theoretical_pace(366.3/4, 36, rate, calibration)),
        "m8+":  sec_to_time(theoretical_pace(352.8/4, 37, rate, calibration)),
        "w1x":  sec_to_time(theoretical_pace(488.7/4, 32, rate, calibration)),
        "w2x":  sec_to_time(theoretical_pace(444.8/4, 34, rate, calibration)),
        "w4x+": sec_to_time(theoretical_pace(422.2/4, 35, rate, calibration)),
        "w4x" : sec_to_time(theoretical_pace(411.4/4, 36, rate, calibration)),
    })
df = pd.DataFrame(list)
df