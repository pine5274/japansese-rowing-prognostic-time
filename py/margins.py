import csv
import pprint
import pandas as pd
import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
from statistics import median
from functools import reduce

def time_to_sec(x):
    if (type(x) is float):
        return x
    minutes = int(x[1])
    seconds = float(x[-5:])
    return minutes * 60 + seconds

def sec_to_time(time):
    m = math.floor(time / 60)
    s = round((time % 60), 1)
    if s < 10:
        return str(m) + ':0' + str(s)
    return str(m) + ':' + str(s)

def plot_margin(x, y, line_y, boat_type):

    fig, ax = plt.subplots()

    plt.plot(x, line_y, ("--"), color="orange")
    plt.scatter(x, y)
    plt.title(f"{boat_type}")
    plt.xlabel('Places from winner', fontsize=12)  # x軸ラベル
    plt.ylabel('Margin from winner (%)', fontsize=12)  # y軸ラベル
    plt.grid()
    plt.show()

years = np.arange(2000, 2024, 1)
types = [
    'm1x',
    'm2x',
    'm4x',
    'm2-',
    # 'm2+',
    'm4-',
    'm4+',
    'm8+',
    'w1x',
    'w2x',
    'w4x',
    # 'w4x+',
    'w2-',
    'w4+',
]

def x_x(a):
    result = 0
    for i, xxx in enumerate(a):
        result = result + a[i] * a[i]
    return result

def x_y(a, b):
    result = 0
    for i, xxx in enumerate(a):
        result = result + a[i] * b[i]
    return result

with open('../../prognostic-time/dst/trends/inter_college/PT_time.csv') as f:
    reader = csv.DictReader(f)
    l_pt = [row for row in reader]

df_all = pd.read_csv('../../rowScraping/dst/inter_college_2023.csv', sep=',')
df_all = df_all[df_all['year'] != 2021]
df_all = df_all.loc[:,['year','boat_type', 'section_code', 'order', '2000m']]
df_all = df_all[df_all['section_code'].str.contains("決勝|Final A|Final B|順決")]

df_A = df_all[df_all['section_code'].str.contains("決勝|Final A")].groupby(['boat_type', 'year'], as_index=False)['2000m'].count()
df_A = df_A.rename(columns={'2000m': 'count_A'})
df_A['winner'] = df_all[df_all['section_code'].str.contains("決勝|Final A")].groupby(['boat_type', 'year'], as_index=False)['2000m'].min()['2000m']
df_A['winner'] = df_A['winner'].map(time_to_sec)
list_countA = df_A.to_dict(orient='records')

d = {}
l = []

for boat_type in types:
    df = df_all[df_all['boat_type'] == boat_type].copy()

    for index, row in df.iterrows():
        f = list(filter(lambda x: x["boat_type"] == row['boat_type'] and x["year"] == row['year'], list_countA))[0]
        second = time_to_sec(row['2000m'])
        order = row['order'] - 1
        df.at[index, '2000m'] = second
        df.at[index, 'percentage'] = round(100 * (second / f['winner'] - 1), 2)
        if row['section_code'] == 'Final B' or row['section_code'] == '順決' :
            count_A = f["count_A"]
            df.at[index, 'order'] = count_A + order
        else:
            df.at[index, 'order'] = order

    p = df['2000m'].quantile(0.003)
    q = df['2000m'].quantile(0.997)
    df = df[(df['2000m'] > p)]
    df = df[(df['2000m'] < q)]
    df = df[df['order'] < 9]
    x = df.loc[:, 'order']
    y = df.loc[:, 'percentage']

    xx = x_x(x.to_list())
    xy = x_y(x.to_list(), y.to_list())
    slope = xy/xx
    line_y = slope * x

    pt = float(list(filter(lambda x: x["boat_type"] == boat_type, l_pt))[0]["PT[s]"])

    d["boat_type"] = boat_type
    d["gap [%]"] = round(slope, 2)
    d["gap [s/2000m]"] = round(pt * slope / 100, 2)
    d["3rd [%IDT]"] = round(100 - slope * 2, 2)
    d["6th [%IDT]"] = round(100 - slope * 5, 2)
    d["8th [%IDT]"] = round(100 - slope * 7, 2)
    d["12th [%IDT]"] = round(100 - slope * 11, 2)
    d["18th [%IDT]"] = round(100 - slope * 17, 2)
    l.append(d)
    d = {}

    # plot_margin(x, y, line_y, boat_type)

margin_df = pd.DataFrame(l)
