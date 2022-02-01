import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 150)

df = pd.read_csv('./../csv/race_scraping2021_second.csv', sep=',')

df.drop(['500m', '1000m', '1500m','team', 'order', 'tournament_name', 'race_number', 'lane', 'Unnamed: 0', 'qualify'], axis=1, inplace=True)
indexNames = df[
    (df['2000m'] == 0.0)
].index
df.drop(indexNames , inplace=True)
final_df = df[df['section_code'].str.contains("準決")]

dropIndex = final_df[ 
    (((final_df['year'] == 2017) | (final_df['year'] == 2019)) & (final_df['boat_type'] == 'm1x')) |
    (((final_df['year'] == 2000) | (final_df['year'] == 2019)) & (final_df['boat_type'] == 'm2x')) |
    (((final_df['year'] == 2000) | (final_df['year'] == 2019)) & (final_df['boat_type'] == 'm2-')) |
    (((final_df['year'] == 2010) | (final_df['year'] == 2019)) & (final_df['boat_type'] == 'm4x')) |
    (((final_df['year'] == 2010) | (final_df['year'] == 2015)) & (final_df['boat_type'] == 'm4+')) |
    (((final_df['year'] == 2010) | (final_df['year'] == 2014)) & (final_df['boat_type'] == 'm4-')) |
    (((final_df['year'] == 2008) | (final_df['year'] == 2010)) & (final_df['boat_type'] == 'm8+')) |
    (((final_df['year'] == 2003) | (final_df['year'] == 2018)) & (final_df['boat_type'] == 'w1x')) |
    (((final_df['year'] == 2013) | (final_df['year'] == 2019)) & (final_df['boat_type'] == 'w2x')) |
    (((final_df['year'] == 2001) | (final_df['year'] == 2019)) & (final_df['boat_type'] == 'w2-')) |
    (((final_df['year'] == 2010) | (final_df['year'] == 2019)) & (final_df['boat_type'] == 'w4x+'))
].index

drop = final_df.drop(dropIndex)
pd.set_option('display.max_rows', None)

median = drop.groupby(['boat_type'])['2000m'].median()


dict = median.to_dict()

diff = {}
for key_i, value_i in dict.items():
    for key_j, value_j in dict.items():
        if key_i == key_j:
            continue
        if (value_i - value_j) < 0 or (value_i - value_j) > 15:
            continue
        key = key_i + ' - ' + key_j
        diff[key] = (value_i - value_j) / 4

diff_df = pd.DataFrame.from_dict(diff, orient="index", columns=["diff"])

diff_df.sort_values('diff').plot(kind='bar') # 棒グラフにする
plt.ylabel("diff / 500m")
plt.title("Differences in the semi-finals by boat type")
plt.show()
plt.savefig("image5.jpg")