import pandas as pd
import datetime
import math

def second_to_time(second):
    return datetime.time(0, int(second//60), int(second%60), round(math.modf(second)[0]*1000000))

df = pd.read_csv('./../csv/race_scraping2021_second.csv', sep=',')

df.drop(['500m', '1000m', '1500m','team', 'order', 'tournament_name', 'race_number', 'lane', 'Unnamed: 0', 'qualify'], axis=1, inplace=True)
indexNames = df[
    (df['2000m'] == 0.0)
].index
df.drop(indexNames , inplace=True)
yosen_df = df[df['section_code'].str.contains('予選')]

Msingle = yosen_df[yosen_df['boat_type'] == 'm1x']
Mdouble = yosen_df[yosen_df['boat_type'] == 'm2x']
Mpair = yosen_df[yosen_df['boat_type'] == 'm2-']
Mquad = yosen_df[yosen_df['boat_type'] == 'm4x']
MfourPlus = yosen_df[yosen_df['boat_type'] == 'm4+']
Mfour = yosen_df[yosen_df['boat_type'] == 'm4-']
Meight = yosen_df[yosen_df['boat_type'] == 'm8+']
Wsingle = yosen_df[yosen_df['boat_type'] == 'w1x']
Wdouble = yosen_df[yosen_df['boat_type'] == 'w2x']
Wpair = yosen_df[yosen_df['boat_type'] == 'w2-']
WquadPlus = yosen_df[yosen_df['boat_type'] == 'w4x+']
Wquad = yosen_df[yosen_df['boat_type'] == 'w4x']
WfourPlus = yosen_df[yosen_df['boat_type'] == 'w4+']


print("M1x")
print(Msingle.groupby(['year'])['2000m'].median())
print("------------")
print("M2x")
print(Mdouble.groupby(['year'])['2000m'].median())
print("------------")
print("M2-")
print(Mpair.groupby(['year'])['2000m'].median())
print("------------")
print("M4x")
print(Mquad.groupby(['year'])['2000m'].median())
print("------------")
print("M4+")
print(MfourPlus.groupby(['year'])['2000m'].median())
print("------------")
print("M4-")
print(Mfour.groupby(['year'])['2000m'].median())
print("------------")
print("M8+")
print(Meight.groupby(['year'])['2000m'].median())
print("------------")
print("W1x")
print(Wsingle.groupby(['year'])['2000m'].median())
print("------------")
print("W2x")
print(Wdouble.groupby(['year'])['2000m'].median())
print("------------")
print("W2-")
print(Wpair.groupby(['year'])['2000m'].median())
print("------------")
print("W4x+")
print(WquadPlus.groupby(['year'])['2000m'].median())
print("------------")
print("W4x")
print(Wquad.groupby(['year'])['2000m'].median())
print("------------")
print("W4+")
print(WfourPlus.groupby(['year'])['2000m'].median())
print("------------")

print("M1x")
print(Msingle.groupby(['year'])['2000m'].median().describe())
print("------------")
print("M2x")
print(Mdouble.groupby(['year'])['2000m'].median().describe())
print("------------")
print("M2-")
print(Mpair.groupby(['year'])['2000m'].median().describe())
print("------------")
print("M4x")
print(Mquad.groupby(['year'])['2000m'].median().describe())
print("------------")
print("M4+")
print(MfourPlus.groupby(['year'])['2000m'].median().describe())
print("------------")
print("M4-")
print(Mfour.groupby(['year'])['2000m'].median().describe())
print("------------")
print("M8+")
print(Meight.groupby(['year'])['2000m'].median().describe())
print("------------")
print("W1x")
print(Wsingle.groupby(['year'])['2000m'].median().describe())
print("------------")
print("W2x")
print(Wdouble.groupby(['year'])['2000m'].median().describe())
print("------------")
print("W2-")
print(Wpair.groupby(['year'])['2000m'].median().describe())
print("------------")
print("W4x+")
print(WquadPlus.groupby(['year'])['2000m'].median().describe())
print("------------")
print("W4x")
print(Wquad.groupby(['year'])['2000m'].median().describe())
print("------------")
print("W4+")
print(WfourPlus.groupby(['year'])['2000m'].median().describe())
print("------------")