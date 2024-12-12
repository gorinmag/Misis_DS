import pandas as pd
import numpy as np
df = pd.read_csv("task_11.csv")
df["lat_1"] = df['lat'].shift(1)
df["lon_1"] = df['lon'].shift(1)

df['dist_trig'] = (np.sin(df['lat_1'])*np.sin(df['lat']) + np.cos(df['lat_1'])*np.cos(df['lat'])*np.cos(df['lon'] - df['lon_1']))
df[df['dist_trig']>1] = 1
df['dist_geo'] = 111.2 * (np.arccos(df['dist_trig']))
df = df.fillna(0)
print(f"Общее расстояние: {df['dist_geo'].sum()} км")