import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('task_21.csv')
df = df.sort_values(by='timestamp')


def haversine(lon1, lat1, lon2, lat2):
    R = 6371.0  # Радиус Земли в километрах
    dlon = np.radians(lon2 - lon1)
    dlat = np.radians(lat2 - lat1)

    a = np.sin(dlat / 2) ** 2 + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))

    return R * c
df['distance'] = haversine(df['lon'].shift(), df['lat'].shift(), df['lon'], df['lat'])
#Игнорирую записи с расстоянием от предыдущей точки более чем 10 км
df_witout_interf = df[df['distance']<10]

plt.title('Общий трек')
plt.plot(df['lat'], df['lon'])
plt.xlabel('Долгота')
plt.ylabel('Широта')
plt.show()
plt.title('Трек без шума')
plt.plot(df_witout_interf['lat'], df_witout_interf['lon'])
plt.xlabel('Долгота')
plt.ylabel('Широта')
plt.show()