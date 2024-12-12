import pandas as pd
import numpy as np

df = pd.read_csv('task_18.csv')
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


def haversine(lon1, lat1, lon2, lat2):
    R = 6371.0  # Радиус Земли в километрах
    dlon = np.radians(lon2 - lon1)
    dlat = np.radians(lat2 - lat1)

    a = np.sin(dlat / 2) ** 2 + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))

    return R * c


def calculate_speed(data):
    df['distance'] = haversine(df['lon'].shift(), df['lat'].shift(), df['lon'], df['lat'])
    df['time_diff'] = (df['timestamp'].diff()) / 3600.0
    df['speed'] = df['distance'] / df['time_diff']
    df.fillna(0, inplace=True)  # или можно оставить NaN для первой точки
    return df[['timestamp', 'speed']]
speed_df = calculate_speed(df)
turn = []
df1 = df
for i in range(len(df1) - 1):
    tr = abs(df1['azimuth'].iloc[i] - df1['azimuth'].iloc[i+1])
    turn.append(tr)
turn.append(np.nan)
df1['turn'] = turn
#Запись является поворотом если азимут изменяется более чем на 20 градусов - статус поворота
df1['turned'] = df1['turn']>20
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
print(f"Средняя скорость при допуске азимута 20 градусов: {df2['speed'].mean().round(2)} км/ч")