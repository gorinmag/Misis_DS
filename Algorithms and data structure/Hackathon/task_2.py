with open("task_2.txt", "r", encoding="utf-8") as f:
    ts2 = f.read().split(' ')
for i in range(len(ts2)):
    if "совершенно" in ts2[i]:
        print(i)
