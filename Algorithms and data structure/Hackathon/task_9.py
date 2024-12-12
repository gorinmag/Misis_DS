import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('task_9.csv')
matches = df[(df['user_agent'].str.contains('Mozilla', case=False, regex=True))]
users = matches["user_agent"].count()
plt.title("Кол-во пользователей которые используют Mozilla")
plt.bar("Mozilla",users)
plt.show()