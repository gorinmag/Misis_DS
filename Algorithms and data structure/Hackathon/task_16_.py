import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

df = pd.read_csv('task_16.csv')
df['timestamp'] = df['timestamp'].astype("datetime64[s]")
df = df.sort_values(by='timestamp')

def calculate_initial_azimuth(lat1, lon1, lat2, lon2):
    lat1_rad = np.radians(lat1)
    lat2_rad = np.radians(lat2)
    delta_lon_rad = np.radians(lon2 - lon1)

    x = np.sin(delta_lon_rad) * np.cos(lat2_rad)
    y = np.cos(lat1_rad) * np.sin(lat2_rad) - np.sin(lat1_rad) * np.cos(lat2_rad) * np.cos(delta_lon_rad)
    azimuth = np.arctan2(x, y)

    azimuth = np.degrees(azimuth)
    azimuth = (azimuth + 360) % 360
    return azimuth
azimuths = []

for i in range(len(df) - 1):
    azimuth = calculate_initial_azimuth(
        df['lat'].iloc[i], df['lon'].iloc[i],
        df['lat'].iloc[i + 1], df['lon'].iloc[i + 1]
    )
    azimuths.append(azimuth)
azimuths.append(np.nan)
df['azimuth'] = azimuths


norm = mcolors.Normalize(vmin=df['timestamp'].min().timestamp(), vmax=df['timestamp'].max().timestamp())
cmap = plt.cm.viridis
plt.figure(figsize=(10, 6))
plt.scatter(df['lon'], df['lat'], c=df['timestamp'].apply(lambda x: x.timestamp()), cmap=cmap, norm=norm)
plt.colorbar(label='Timestamp')
plt.xlabel('Долгота')
plt.ylabel('Широта')
plt.title('Карта движения')
plt.grid()
plt.show()
plt.figure(figsize=(10, 6))
plt.plot(df['timestamp'], df['azimuth'])
plt.xlabel('Время')
plt.ylabel('Азимут')
plt.title('График изменения азимута движения')
plt.grid()
plt.show()