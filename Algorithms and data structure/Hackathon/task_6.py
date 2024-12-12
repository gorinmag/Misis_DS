import pandas as pd
ls = ["0","1",'2','3','4','5','6','7','8','9']
ls1 =[]
df = pd.read_csv('task_6.csv')
for i in df['email']:
    for j in ls:
        if j in i:
            ls1.append(i)
ls = list(set(ls1))
print(f"Кол-во людей содержащих цифры в email: {len(ls)}")