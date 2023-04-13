import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from statistics import median

def speed(x):
    return 2000 / x

def plot_trends(df, boat_type):
    # 外れ値の除去
    q = df['2000m'].quantile(0.954)
    df = df[(df['2000m'] < q)]

    x = df.loc[:, 'year']
    y = df.loc[:, '2000m']      
    y = y.map(speed)
    #近似式の係数
    res1=np.polyfit(x, y, 1)
    res2=np.polyfit(x, y, 2)
    res3=np.polyfit(x, y, 3)
    #近似式の計算
    y1 = np.poly1d(res1)(x) #1次
    y2 = np.poly1d(res2)(x) #2次
    y3 = np.poly1d(res3)(x) #3次

    # 2022年の推定値
    PT_1 = np.poly1d(res1)(2023)
    PT_2 = np.poly1d(res2)(2023)
    PT_3 = np.poly1d(res3)(2023)
    #グラフ表示
    plt.scatter(x, y, label='time')
    plt.plot(x, y1, label='1d')
    plt.plot(x, y2, label='2d')
    plt.plot(x, y3, label='3d')
    plt.xticks(np.arange(2000, 2023, 2))
    plt.title(boat_type + " trends")
    plt.xlabel('year', fontsize=12)  # x軸ラベル
    plt.ylabel('speed[m/s]', fontsize=12)  # y軸ラベル
    plt.grid()
    plt.legend()
    plt.savefig('./../dst/trends/all_japan/' + boat_type + '.jpg')
    plt.figure()

    return  median([PT_1, PT_2, PT_3])

def sec_to_time(time):
    m = math.floor(time / 60)
    s = round((time % 60), 1)
    if s < 10:
        return str(m) + ':0' + str(s)
    return str(m) + ':' + str(s)

df = pd.read_csv('./../csv/all_japan_second.csv', sep=',')
df.drop(['500m', '1000m', '1500m','team', 'order', 'race_number', 'lane', 'Unnamed: 0', 'qualify'], axis=1, inplace=True)
indexNames = df[
    (df['2000m'] == 0.0)
].index
df.drop(indexNames , inplace=True)
final_df = df[df['section_code'].str.contains("決勝|Final A")]
pd.set_option('display.max_rows', None)
winner = final_df.groupby(['boat_type', 'year'], as_index=False)['2000m'].min()
boat_types = (winner['boat_type'].unique())

dict = {}

for v in boat_types:
    boat = winner[winner['boat_type'] == v]
    # if (v == 'w4x') | (v == 'w4+'):
    #     continue
    PT = plot_trends(boat, v)
    dict[v] = sec_to_time(round((2000 / PT), 1))
    # dict[v] = round((2000 / PT), 1)

# for k in dict.keys():
#     dict[k] = sec_to_time(dict[k])

# print(dict)
pt_df = pd.DataFrame.from_dict(dict, orient="index", columns=["PT"])
pt_df.to_csv('./../dst/trends/all_japan/PT_time.csv')