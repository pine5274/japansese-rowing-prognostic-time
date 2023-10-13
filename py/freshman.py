import pandas as pd
import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
from statistics import median

def plot_trends(x, y, y1, y2, y3, boat_type):
    fig, ax = plt.subplots()
    ax.invert_yaxis()
    ax.yaxis.set_major_formatter(mpl.ticker.FuncFormatter(sec_to_time_lamda))
    plt.scatter(x, y, label='time')
    plt.plot(x, y1, label='1d')
    # plt.plot(x, y2, label='2d')
    # plt.plot(x, y3, label='3d')
    plt.xticks(np.arange(2000, 2023, 2))
    plt.title(boat_type + " trends")
    plt.xlabel('year', fontsize=12)  # x軸ラベル
    plt.ylabel('time', fontsize=12)  # y軸ラベル
    plt.grid()
    plt.legend()
    plt.savefig('./../dst/trends/freshman/' + boat_type + '.jpg')
    plt.figure()

def sec_to_time_lamda(time, pos):
    m = math.floor(time / 60)
    s = round((time % 60), 1)
    if s < 10:
        return str(m) + ':0' + str(s)
    return str(m) + ':' + str(s)

def sec_to_time(time):
    m = math.floor(time / 60)
    s = round((time % 60), 1)
    if s < 10:
        return str(m) + ':0' + str(s)
    return str(m) + ':' + str(s)

df = pd.read_csv('./../csv/freshman_second.csv', sep=',')
df = df[df['section_code'].str.contains("決勝|Final A")]
df = df.groupby(['boat_type', 'year'], as_index=False)['2000m'].min()

boat_types = (df['boat_type'].unique())
l = []
d = {}
for boat_type in boat_types:
    if boat_type == 'w4+':
        continue
    df_bt = df[df['boat_type'] == boat_type]
    q = df_bt['2000m'].quantile(0.954)
    df_bt = df_bt[(df_bt['2000m'] < q)]
    x = df_bt['year'].unique()
    y = df_bt.loc[:, '2000m']
    res1=np.polyfit(x, y, 1)
    res2=np.polyfit(x, y, 2)
    res3=np.polyfit(x, y, 3)
    #近似式の計算
    y1 = np.poly1d(res1)(x) #1次
    y2 = np.poly1d(res2)(x) #2次
    y3 = np.poly1d(res3)(x) #3次

    # 2023年の推定値
    PT_1 = np.poly1d(res1)(2023)
    PT_2 = np.poly1d(res2)(2023)
    PT_3 = np.poly1d(res3)(2023)

    #グラフ表示
    plot_trends(x, y, y1, y2, y3, boat_type)
    d['boat_type'] = boat_type
    d['PT'] = sec_to_time(PT_1)
    d['delta[s]'] = round(res1[0], 2)
    l.append(d)
    d = {}

pt_df = pd.DataFrame(l)

# pt_df.to_csv('./../dst/trends/inter_college/PT_time.csv')