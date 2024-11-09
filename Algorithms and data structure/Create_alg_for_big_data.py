import db_class
import matplotlib.pyplot as plt
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
plt.scatter(ls[0],ls[1])
plt.scatter(time_lim, speed, color = "red")
plt.plot()

plt.show()
