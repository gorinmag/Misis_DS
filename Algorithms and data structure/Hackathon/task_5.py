import csv
sm = 0
with open("task_5.csv", newline='') as f:
    ts5 = csv.reader(f, delimiter=' ')
    for row in ts5:
       try:
            sm += int(row[0])
       except ValueError:
           continue
print(f"Сумма строк столбца number: {sm}")