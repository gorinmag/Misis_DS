with open("task_3.txt", "r", encoding="utf-8") as f:
    ts3 = f.read().split(' ')
dot = 0
comma = 0
for i in range(len(ts3)):
    if "," in ts3[i]:
        comma +=1
    if "." in ts3[i]:
        dot +=1
print(f"Кол-во точек: {dot}, Кол-во запятых: {comma}")