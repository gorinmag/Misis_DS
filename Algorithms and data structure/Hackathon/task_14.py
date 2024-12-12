import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
df = pd.read_csv("task_14.csv")
df = df.sort_values(by='timestamp')
df["lat_1"] = df['lat'].shift(1)
df["lon_1"] = df['lon'].shift(1)
df['timestamp_1'] = df['timestamp'].shift(1)
df['timestamp_1'] = df['timestamp_1'].fillna(1727724956)
df['time_from'] = pd.to_datetime(df['timestamp_1'],unit = 's')
df['time_to'] = pd.to_datetime(df['timestamp'], unit='s')
df['dist_trig'] = (np.sin(df['lat_1'])*np.sin(df['lat']) + np.cos(df['lat_1'])*np.cos(df['lat'])*np.cos(df['lon'] - df['lon_1']))
df[df['dist_trig']>1] = 1
df['dist_geo'] = 111.2 * (np.arccos(df['dist_trig']))
df = df.fillna(0)
df['timedelta'] = (df['time_to'] - df['time_from']).astype("timedelta64[ns]")
df['hour'] = (df['timedelta'].dt.total_seconds()/3600).round(5)
df['speed'] = df['dist_geo']/df['hour']
df['hourly'] = (df['timestamp'].astype("datetime64[s]")).dt.strftime('%Y-%m-%d %H')
df1 = df[df['speed']==0]
print(f"Кол-во остановок для каждого часа: {df1.groupby(['hourly'])['hourly'].count()}")
dc = (df1.groupby(['hourly'])['hourly'].count()).to_dict()
plt.bar(dc.keys(), dc.values())
plt.show()