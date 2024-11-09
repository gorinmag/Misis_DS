from cgi import print_environ_usage
from random import randint, randrange
from traceback import print_tb

import psycopg2
import random
import matplotlib.pyplot as plt
conn = psycopg2.connect(user = 'test', password = '123', database = 'ivan')
cursor = conn.cursor()
#Задание 1_1
#Создание таблицы
cursor.execute('create table aero1 (city text, company text, date timestamp)')
conn.commit()
# #Импорт данных в таблицу из файла csv
cursor.execute(r"copy aero1 from 'D:\aero.csv' delimiter ',' csv header;")
conn.commit()

# Задание 1_2
#Самолеты от Аэрофлота
company = "Aeroflot"
cursor.execute('select * from aero1 where company = %s;', (company,) )
query1 = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
print(query1)

#Задание 1_3
# Самолеты не принадлежавшие Аэрофлоту
cursor.execute('select * from aero1 where company != %s', (company,))
query2 = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
print(query2)

#Задание 1_5
# Удалить все данные из таблицы
cursor.execute('delete from aero1')
conn.commit()

#Задание 1_7
#Изменить данные для компании Аэрофлот на Аэрофлот 2
company2 = 'Aeroflot 2'
cursor.execute('update aero1 set company = %s where company = %s', (company2, company,))
conn.commit()
cursor.execute('select * from aero1  where company = %s', (company2,))
query3 = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
print(query3)


#Задание 1_8
# Удалить все данные о компании S7
cursor.execute("delete from aero1 where company = 'S7'")
conn.commit()
cursor.execute("select *  from aero1")
query4 = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
print(query4)

#Задание 2
#Создать таблицу с x и y
cursor.execute('create table data (x integer, y integer)')
conn.commit()

#Задание 3
# Заполнить таблицу сгенерированными данными
x = [i for i in range(1,30)]
y = [randint(1,100) for i in range(30)]
for i in range(29):
    cursor.execute('insert into data (x, y) values (%s, %s)',(x[i], y[i]),)
    conn.commit()

#Задание 4
#Получить данные из таблицы
cursor.execute('select * from data')
query5 = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
#Задание 5
# Заполнить 2 списка данными из таблицы
x_ = []
y_ = []
for i in query5:
    x_.append(i["x"])
    y_.append(i["y"])
#Задание 6
#Построить график по полученным данным
plt.bar(x_, y_)
plt.title("График по полученным данным")
plt.xlabel("x_ - порядковый номер")
plt.ylabel('y_ - случайное значение')
plt.show()
cursor.close()
conn.close()