import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import csv

def sec_to_time(time):
    m = math.floor(time / 60)
    s = round((time % 60), 1)
    if s < 10:
        return str(m) + ':0' + str(s)
    return str(m) + ':' + str(s)

def theoretical_pace(target_time, target_rate, rate=34, calibration = 1):
    return target_time/4/(rate/target_rate)**(calibration*(1/3))


with open('../csv/target_time.csv') as f:
    reader = csv.DictReader(f)
    l = [row for row in reader]

x_rate_list = np.arange(16, 41, 4)
calibration = 0.7

for d in l:
    for x in x_rate_list:
        d[f'SR: {x}'] = sec_to_time(theoretical_pace(float(d['target_time']), int(d['target_rate']), x, calibration))
    d['target_time'] = sec_to_time(float(d['target_time']))
    
df = pd.DataFrame(l)
df.to_csv('../dst/theoretical_pace.csv')
x_SR = np.arange(16, 42, 0.5)
y = []
calibration = np.arange(0.65, 1.05, 0.05)
for c in calibration:
    for x in x_SR:
        y.append(theoretical_pace(120, 20, x, c))
    plt.plot(x_SR, y, label=c)
    y = []
    
plt.figure()