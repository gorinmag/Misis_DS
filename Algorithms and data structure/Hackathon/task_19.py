import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('task_19.csv')
df = df.sort_values(by='timestamp')
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
actions = df.groupby(df['timestamp'].dt.date).size().to_dict()
#Убираю незначимые действия
filtered_df = (df[~df['url'].str.startswith('/')][~df['url'].str.startswith('?')])
page_visits = filtered_df['url'].value_counts()
# print(filtered_df)

filtered_df['operation'], filtered_df['file'] = filtered_df['url'].str.split('/', 1).str
file_operations = (filtered_df.groupby(['operation', 'file']).size().unstack(fill_value=0)).sum(axis=1)
# print(file_operations.sum(axis=1))
#Собираю данные в словарь по удалению и добавлению файлов
act_point = {}
act_point['del'] = df[df['url'].str.startswith('/del')]['url'].count()
act_point['add'] = df[df['url'].str.startswith('/add')]['url'].count()
# Собираю данные о регистрации входов в систему
df_login = df[df['url']=='login']
df_login['hourly'] = (df_login['timestamp'].astype("datetime64[s]")).dt.strftime('%Y-%m-%d %H')
login_group = df_login.groupby(df_login['hourly']).size()
print(login_group)



#График 1 активность пользователей
plt.bar(actions.keys(),actions.values())
plt.title('Временная диаграмма действий пользователей')
plt.xlabel('Дата')
plt.ylabel('Количество действий')
plt.show()

#График 2 Посещаемость страниц
page_visits.plot(kind = 'bar')
plt.title('Посещаемость страниц')
plt.xlabel('Адрес')
plt.ylabel('Количество действий')
plt.show()


#График 3 загрузка и выгрузка
file_operations.plot(kind='bar')
plt.title('Диаграмма загрузки и выгрузки файлов')
plt.xlabel('Действие')
plt.ylabel('Количество операций')
plt.xticks(rotation=90)
plt.grid()
plt.show()

#График 4 удаление и добавление
plt.title('Диаграмма добавления и удаления файлов')
plt.bar(act_point.keys(),act_point.values())
plt.xlabel('Действие')
plt.ylabel('Количество операций')
plt.grid()
plt.show()

#График 5 регистрации пользователей
plt.title('График регистрации пользователей по часам')
login_group.plot()
plt.xlabel('Дата')
plt.ylabel('Кол-во регистраций')
plt.grid()
plt.show()