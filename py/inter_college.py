import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from statistics import median

def speed(x):
    return 2000 / x

def calc_PT(df, boat_type):
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
    # plot_trends(x, y, y1, y2, y3, boat_type)

    return  median([PT_1, PT_2, PT_3])

def plot_trends(x, y, y1, y2, y3, boat_type):
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
    plt.savefig('./../dst/trends/inter_college/' + boat_type + '.jpg')
    plt.figure()

def sec_to_time(time):
    m = math.floor(time / 60)
    s = round((time % 60), 1)
    if s < 10:
        return str(m) + ':0' + str(s)
    return str(m) + ':' + str(s)

def generate_PT_list(boat_types):
    l = []
    d = {}
    for boat_type in boat_types:
        if (boat_type == 'w4x'):
            continue
        boat = df[df['boat_type'] == boat_type]
        PT = calc_PT(boat, boat_type)
        PT_seconds = round((2000 / PT), 1)
        d['boat_type'] = boat_type
        d['PT'] = sec_to_time(PT_seconds)
        d['PT[s]'] = PT_seconds
        l.append(d)
        d = {}

    return l;

def adjustment(l):
    for d in l:
        if (d['boat_type'] == 'm8+'):
            v_standard = d['PT[s]']
        if (d['boat_type'] == 'm2x'):
            double = d['PT[s]']
        if (d['boat_type'] == 'm4x'):
            quad = d['PT[s]']

    double_to_quad = quad / double

    for d in l:
        d['ratio'] = round(d['PT[s]']/ v_standard, 3)
        if (d['boat_type'] == 'w2x'):
            PTw4x = round(d['PT[s]'] * double_to_quad, 1)

    l.append({
        'boat_type': 'w4x',
        'PT': sec_to_time(PTw4x),
        'PT[s]': PTw4x,
        'ratio': round(PTw4x / v_standard, 3)
    })

    return l

df = pd.read_csv('./../csv/inter_college_second.csv', sep=',')
df = df[df['section_code'].str.contains("決勝|Final A")]
df = df.groupby(['boat_type', 'year'], as_index=False)['2000m'].min()
# 2021年は全日本と合同開催なので除去
df = df[df['year'] != 2021]
# 2021年のデータを手動で読み込む
df_2021 = pd.read_csv('./../csv/inter_college_2021.csv', sep=',')
df = pd.concat([df, df_2021])

boat_types = (df['boat_type'].unique())
l = generate_PT_list(boat_types)
l = adjustment(l)
pt_df = pd.DataFrame(l)



# pt_df = pd.DataFrame.from_dict(dict, orient="index", columns=["PT"])
pt_df.to_csv('./../dst/trends/inter_college/PT_time.csv')