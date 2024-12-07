
import db_class
import matplotlib.pyplot as plt
from datetime import datetime as dt
# Задание 1
conn = db_class.ConnectionDB(login="test", password="123", database="exer")
tp = conn.get_data_speed()
ls = [[],[]]

for i in tp:
    ls[0].append(int(i["timestamp"]))
    ls[1].append([i["speed"]])


def sort (arg,kvarg):
  for i in range(len(arg)-1):
      for j in range(len(arg)-1-i):
          if arg[j] > arg[j+1]:
              arg[j], arg[j+1] = arg[j+1], arg[j]
              kvarg[j], kvarg[j + 1] = kvarg[j + 1], kvarg[j]
sort(ls[0],ls[1])
time_lim = []
speed = []

t = 0
for i in ls[1]:
    if i[0] > 60:
         print(f"Cкорость превышена на {i[0]-60}")
         time_lim.append(ls[0][t])
         speed.append(ls[1][t])
    t=t+1
t = 0
p=0
ls_1 = [ls[0][0]]
for i in ls[0]:
    if (i - ls_1[p]) > 300:
        ls_1.append(i)
        p+=1
db_class.ConnectionDB.close_db(self=conn)
plt.scatter(ls[0],ls[1],s=0.2)
plt.scatter(time_lim, speed, color = "red",s=0.4)
plt.plot()

plt.show()


#Задание 2*
# data = conn.get_speed_for2task()
# fuel = []
# time = []
# dict_fuel = {'time': [], 'fuel': []}
# time_refresh=[]
# fuel_delta = []
# for i in data:
#     try:
#         dict_fuel['fuel'].append(i['can_data']['fuel_tank_litrage'])
#         dict_fuel['time'].append(dt.fromtimestamp(i['timestamp']))
#
#     except KeyError:
#         continue
# db_class.ConnectionDB.close_db(self=conn)
# sorted_fuel = sorted(dict_fuel.items(), key=lambda item: item[0])
# for i in range(len(sorted_fuel[0][1])):
#     try:
#         if sorted_fuel[0][1][i+1] - sorted_fuel[0][1][i] > 10:
#             time_refresh.append(sorted_fuel[1][1][i])
#             fuel_delta.append(sorted_fuel[0][1][i+1] - sorted_fuel[0][1][i])
#             print("Заправка", sorted_fuel[0][1][i+1] - sorted_fuel[0][1][i])
#     except IndexError:
#         continue
# plt.scatter(sorted_fuel[1][1], sorted_fuel[0][1], s = 0.4)
# for i in range(len(time_refresh)):
#     plt.axvline(x = time_refresh[i], label = "Заправка", color = 'red')
#     plt.text(time_refresh[i],30, round(fuel_delta[i], 1), rotation = 90, va = 'center')
# plt.show()