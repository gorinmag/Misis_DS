with open("task_1.txt", "r", encoding="utf-8") as f:
    ts1 = f.readlines()
indx = 0
for i in ts1:
    indx = indx+1
    if "салфеткой" in i:
        print("строка содержащая искомое слово:")
        print(i)
        print(f"Номер строки: {indx}")