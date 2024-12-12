import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('task_17.csv')
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
turn = []
df1 = df
for i in range(len(df1) - 1):
    tr = abs(df1['azimuth'].iloc[i] - df1['azimuth'].iloc[i+1])
    turn.append(tr)
turn.append(np.nan)
df1['turn'] = turn
#Запись является поворотом если азимут изменяется более чем на 10 градусов - статус поворота
df1['turned'] = df1['turn']>10
#Счетчик поворотов
id_turn = 0
count_turn = []
for i in range(len(df1) - 1):
    if abs(df1['turned'].iloc[i] == df1['turned'].iloc[i-1]):
        count_turn.append(id_turn)
    else:
        id_turn+=1
        count_turn.append(id_turn)
count_turn.append(np.nan)
df1['count_turn'] = count_turn
df1.to_csv('task_17_df.csv', sep = ',')
df2 = df1[df1['turned']==True]
print(f"Общее число поворотов при допуске азимута 10 градусов: {df1['count_turn'].max()}")
plt.figure(figsize=(10, 6))
plt.scatter(df1['lat'], df1['lon'])
plt.scatter(df2['lat'], df2['lon'], c = 'red')
plt.xlabel('Широта')
plt.ylabel('Долгота')
plt.title('График изменения азимута движения')
plt.legend(['Координата на треке', 'Координата со статусом поворота'])
plt.grid()
plt.show()