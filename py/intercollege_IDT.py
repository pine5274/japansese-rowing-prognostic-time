import pandas as pd
import datetime
import math

df = pd.read_csv('./../csv/race_scraping2021_second.csv', sep=',')

df.drop(['500m', '1000m', '1500m','team', 'order', 'tournament_name', 'race_number', 'lane', 'Unnamed: 0', 'qualify'], axis=1, inplace=True)
indexNames = df[
    (df['2000m'] == 0.0)
].index
df.drop(indexNames , inplace=True)
final_df = df[df['section_code'].str.contains("準決")]
# final_df = df[df['section_code'].str.contains("決勝|順決")]

dict = {}

dropIndex = yosen_df[
    (yosen_df['year'] == 2017) |
    (yosen_df['year'] == 2019)
].index
dict["m1x"]  = final_df[final_df['boat_type'] == 'm1x']
dict["m2x"]  = final_df[final_df['boat_type'] == 'm2x']
dict["m2-"]  = final_df[final_df['boat_type'] == 'm2-']
dict["m4x"]  = final_df[final_df['boat_type'] == 'm4x']
dict["m4+"]  = final_df[final_df['boat_type'] == 'm4+']
dict["m4-"]  = final_df[final_df['boat_type'] == 'm4-']
dict["m8+"]  = final_df[final_df['boat_type'] == 'm8+']
dict["w1x"]  = final_df[final_df['boat_type'] == 'w1x']
dict["w2x"]  = final_df[final_df['boat_type'] == 'w2x']
dict["w2-"]  = final_df[final_df['boat_type'] == 'w2-']
dict["w4x+"] = final_df[final_df['boat_type'] == 'w4x+']
dict["w4x"]  = final_df[final_df['boat_type'] == 'w4x']
dict["w4+"]  = final_df[final_df['boat_type'] == 'w4+']

for key, value in dict.items():
    print(key)
    print(value['2000m'].mean())
    print("------------------")