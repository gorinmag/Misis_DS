import json
data = {}
with open('olympics.json', 'r') as file:
    js_dict = json.load(file)
for i in range(len(js_dict)):
    for k, v in js_dict[i].items():
        if type(v) is int:


# a1 = str(1)
# print(type(a1))
# if type(a1) is int:
#     print('yes')
# else:
#     print('NO')