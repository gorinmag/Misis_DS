import json

# 1 task
input_string = '{"street": "Большая Дмитровка","city": "Москва","country": "Россия"}'
data = json.loads(input_string)
for i in sorted(data.keys()):
    print(f'{i}: {data[i]}')
# 2 task
input_string_2 = 'street: Большая Дмитровка, city : Москва, country: Россия'
data_2 = {}
for i in input_string_2.split(','):
    a = i.strip().split(':')
    b = a[1].strip()
    data_2[a[0]] = b
json_object = json.dumps(data_2, indent = 4,ensure_ascii=False)
print(json_object)
with open("json_task2.json", "w", encoding='utf-8') as f:
    f.write(json_object)
# task 3
with open('input_task_3.json', 'r') as f:
    data_3 = json.load(f)
ls = []
c = 0
for i in data_3:
    if isinstance(i, str):
        ls.append(i+"!")
    elif isinstance(i, float):
        ls.append(i+1)
    elif isinstance(i, bool):
        print(i)
        ls.append(not i)
    elif isinstance(i,int):
        ls.append(i+1)
    elif isinstance(i,list):
        ls.append(i*2)
    elif isinstance(i, dict):
        i["newkey"] = None
        ls.append(i)
data_json_3 = json.dumps(ls)
with open('json_task3.json', 'w', encoding='utf-8') as f:
    f.write(data_json_3)
# task 4
with open('input_task_4.json', 'r', encoding = 'utf-8') as f:
    json_list = json.load(f)
def merge_json_objects(json_list):
    obj1 = json_list[0]
    obj2 = json_list[1]
    result = obj1.copy()
    for key, value in obj2.items():
        if key not in result or key in obj1:
            result[key] = value
    return result

output = merge_json_objects(json_list)
print(json.dumps(output, ensure_ascii=False, indent=4))
# task 5
data = [
    {"firstName": "Иван", "middleName": "Петров", "birthDate": "2001/02/29"},
    {"firstName": "Пётр", "middleName": "Иванов", "city": "Moscow"}
]
all_keys = set()
for obj in data:
    all_keys.update(obj.keys())
for obj in data:
    for key in all_keys:
        if key not in obj:
            obj[key] = None

print(json.dumps(data, ensure_ascii=False, indent=4))
# task 6_1
with open('wifi.json' ,'r') as f:
    data = json.load(f)
dict_district  = {}
for i in data:
    district = i['District']
    dict_district[district] = 0
for i in data:
    district = i['District']
    number_of_access_point = i['NumberOfAccessPoints']
    dict_district[district] += number_of_access_point
print(dict_district)
sorted_districts = sorted(dict_district.items(), key=lambda x: (-x[1], x[0]))
for district, total in sorted_districts:
    print(f"{district}: {total}")
# task 6_2
with open('olympics.json' ,'r') as f:
    data = json.load(f)
leaders  = {}
for i in data:
    name = i['ShortName']
    leaders[name] = [0,0,0]
for i in data:
    if i['Status'] =='победитель' and i['Stage'] == '3':
        leaders[i['ShortName']][0] += 1
        leaders[i['ShortName']][2] += 1
    if i['Status'] == 'призёр' and i['Stage']=='3':
        leaders[i['ShortName']][1] += 1
        leaders[i['ShortName']][2] += 1
sorted_leaders = sorted(leaders.items(), key=lambda x: (-x[1][2],-x[1][0], x[0]))

for name, total in sorted_leaders:
    print(f"{name}: {total[0]} {total[1]}" )

# task 6_3
with open('olympics.json' ,'r') as f:
    data = json.load(f)
objects = {}
for i in data:
    if i["OlympiadType"] == 'Московская олимпиада':
        profile = i['OlympiadProfile'].capitalize()
        objects[profile] = []
for i in data:
    if i["OlympiadType"] == 'Московская олимпиада':
        profile = i['OlympiadProfile'].capitalize()
        objects[profile].append(i["Year"])
sorted_objects = sorted(objects.items(), key=lambda x: (x[0]))

for key, val in sorted_objects:
    print(f"{key}: {len(set(val))}")
