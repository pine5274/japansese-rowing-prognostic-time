import pandas as pd
import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
from statistics import median

def time_to_sec(x):
    if (type(x) is float):
        return x
    time = x.split(':')
    minutes = int(time[0][1])
    seconds = float(time[1])
    return minutes * 60 + seconds

def sec_to_time(time):
    m = math.floor(time / 60)
    s = round((time % 60), 1)
    if s < 10:  
        return str(m) + ':0' + str(s)
    return str(m) + ':' + str(s)

def sec_to_time_lamda(time, pos):
    m = math.floor(time / 60)
    s = round((time % 60), 1)
    if s < 10:
        return str(m) + ':0' + str(s)
    return str(m) + ':' + str(s)

def calc_PT(df, boat_type):
    # 外れ値の除去
    q = df['2000m'].quantile(0.954)
    df = df[(df['2000m'] < q)]

    x = df.loc[:, 'year']
    y = df.loc[:, '2000m']      
    # y = y.map(speed)
    #近似式の係数
    res1=np.polyfit(x, y, 1)
    # res2=np.polyfit(x, y, 2)
    # res3=np.polyfit(x, y, 3)
    #近似式の計算
    y1 = np.poly1d(res1)(x) #1次
    # y2 = np.poly1d(res2)(x) #2次
    # y3 = np.poly1d(res3)(x) #3次

    # 2023年の推定値
    PT_1 = np.poly1d(res1)(2024)
    # PT_2 = np.poly1d(res2)(2023)
    # PT_3 = np.poly1d(res3)(2023)

    # return  median([PT_1, PT_2, PT_3])
    return PT_1

def plot_trends(df, boat_type):
    for boat_type in boat_types:
        category = df[df['boat_type'] == boat_type]
        # 外れ値の除去
        q = category['2000m'].quantile(0.954)
        category = category[(category['2000m'] < q)]

        x = category.loc[:, 'year']
        y = category.loc[:, '2000m']
        res1=np.polyfit(x, y, 1)
        y1 = np.poly1d(res1)(x)


        fig, ax = plt.subplots()
        ax.invert_yaxis()
        ax.yaxis.set_major_formatter(mpl.ticker.FuncFormatter(sec_to_time_lamda))
        plt.scatter(x, y, label='time')
        plt.plot(x, y1, label='trend')
        plt.xticks(np.arange(2000, 2023, 2))
        plt.title(boat_type + " trends")
        plt.xlabel('year', fontsize=12)  # x軸ラベル
        plt.ylabel('time', fontsize=12)  # y軸ラベル
        plt.grid()
        plt.legend()
        plt.savefig('./../dst/trends/all_japan/' + boat_type + '.jpg')
        plt.figure()

def generate_PT_list(df, boat_types):
    l = []
    d = {}
    for boat_type in boat_types:
        category = df[df['boat_type'] == boat_type]
        PT_seconds = calc_PT(category, boat_type)
        d['boat_type'] = boat_type
        d['PT'] = sec_to_time(PT_seconds)
        l.append(d)
        d = {}

    return l;

df = pd.read_csv('./../csv/all_japan_2023.csv', sep=',')
df = df[df['section_code'].str.contains("決勝|Final A")]
df = df[['year', 'boat_type', '2000m']]
df = df.dropna(subset=['2000m'])
df['2000m'] = df['2000m'].map(time_to_sec)
df = df.groupby(['boat_type', 'year'], as_index=False)['2000m'].min()

boat_types = (df['boat_type'].unique())
l = generate_PT_list(df, boat_types)
plot_trends(df, boat_types)
pt_df = pd.DataFrame(l)
