import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("task_10.csv")
df['brow'] = [i[:i.find("/")] for i in df['user_agent']]
ct = df.groupby(['brow'])['brow'].count().to_dict()
plt.bar(ct.keys(), ct.values())
plt.show()