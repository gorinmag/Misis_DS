import pandas as pd
df = pd.read_csv('task_7.csv')
p = df['phone_number']
sm = 0
for i in p:
    if '+7' in i:
        sm +=1
print(f'Кол-во номеров с кодом страны +7: {sm}')
