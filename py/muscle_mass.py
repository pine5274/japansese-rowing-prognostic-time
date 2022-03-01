import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import math

def datetime_serialize(day):
    dt = datetime.datetime.strptime(day, '%Y/%m/%d') - datetime.datetime(2021, 9, 1)
    return dt.days

sheet_name = 'ohira'
df = pd.read_csv('./prognostic-time/csv/' + sheet_name + '.csv', sep=',')
# 外れ値の除去
q = df['muscle_mass'].quantile(0.954)
df = df[(df['muscle_mass'] < q)]
x = df.loc[:, 'day'].map(datetime_serialize)
y = df.loc[:, 'muscle_mass']
print(df)

#近似式の係数
res1=np.polyfit(x, y, 1)
res2=np.polyfit(x, y, 2)
res3=np.polyfit(x, y, 3)
#近似式の計算
y1 = np.poly1d(res1)(x) #1次
y2 = np.poly1d(res2)(x) #2次
y3 = np.poly1d(res3)(x) #3次
plt.scatter(x, y, label='muscle mass')
plt.plot(x, y1, label='1d')
plt.plot(x, y2, label='2d')
plt.plot(x, y3, label='3d')
plt.title(sheet_name + " mascle mass transition")
plt.xlabel('day', fontsize=12)  # x軸ラベル
plt.ylabel('muscle mass [kg]', fontsize=12)  # y軸ラベル
plt.grid()
plt.legend()
plt.figure()