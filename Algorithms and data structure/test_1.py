# Задание 1
# Сделайте функцию, которая параметром будет принимать список и удалять из него все дубли
print("Задача 1")
a = [1,2,3,4,4,3,6,7,2]
def del_duplicates(ls):
 print(set(ls))
del_duplicates(a)

# Задание 2
# Создайте функцию, которая вернет текущий день недели словом
import datetime as dt
print("Задача 2")
def day_week():
  day = (dt.datetime.now()).weekday()
  if day == 0:
    print("Понедельник")
  elif day ==1:
    print("Вторник")
  elif day ==2:
    print('Среда')
  elif day == 3:
    print ("Четверг")
  elif day ==4:
    print("Пятнтица")
  elif day ==5:
    print("Суббота")
  elif day ==6:
    print("Воскресенье")
  else:
    print("Неправильно введен день недели")
  print (dt.datetime.now())
day_week()

#Задание 3
# Сделайте функцию, которая параметром будет получать дату, а возвращать день недели словом, соответствующий этой дате.
print("Задача 3")
import datetime as dt
your_date = input("Введите дату:").split('.')
def data_week (day):
  data = dt.date(int(day[2]), int(day[1]), int(day[0]))
  day = data.weekday()
  if day == 0:
    print("Понедельник")
  elif day ==1:
    print("Вторник")
  elif day ==2:
    print('Среда')
  elif day == 3:
    print ("Четверг")
  elif day ==4:
    print("Пятнтица")
  elif day ==5:
    print("Суббота")
  elif day ==6:
    print("Воскресенье")
  else:
    print("Неправильно введен день недели")
data_week(your_date)

#Задание 4
# Сделайте функцию, которая параметром будет принимать секунды, а возвращать количество суток, соответствующих этим секундам
print("Задача 4")
import datetime
sec = int(input("Введите секунды:"))
def sec_to_day(second):
  dt = datetime.datetime.fromtimestamp(second)
  dt_orig = datetime.datetime.fromtimestamp(0)
  d = dt - dt_orig
  print(d.days)
sec_to_day(sec)

#Задание 5
# Сделайте функцию, которая параметром будет получать дату, а возвращать знак зодиака, соответствующий этой дате.
print("Задача 5")
from datetime import datetime as dt
zodiac = {
    "Овен": [10321,10419],
    "Телец": [10420,10520],
    "Близнецы": [10521,10620],
    "Рак": [10621,10722],
    "Лев": [10723,10822],
    "Дева": [10823,10922],
    "Весы": [10923,11022],
    "Скорпион": [11023,11121],
    "Стрелец": [11122,11221],
    "Козерог": [11222,11231],
    "Козерог": [10101,10119],
    "Водолей": [10120,10218],
    "Рыбы": [10219,10320]}

your_date = input("Введите дату: ").split(".")
def znak (day):
  d = int(str(1) + str(your_date[1]) + str(your_date[0]))
  for k,v in zodiac.items():
    if v[0] <= d <= v[1]:
      print("Ваш знак зодиака:", k)
znak (your_date)

#Задание 6
#  Сделайте функцию, которая будет возвращать сколько дней прошло или осталось до заданной даты в году, в зависимости от того, была уже эта дата или нет
import datetime as dt
print("Задача 6")
your_date = input("Введите дату:").split(".")
def ostatok (day):
  data = dt.datetime(int(day[2]), int(day[1]), int(day[0]))
  current = dt.datetime.now()
  ost = (data - current)
  if ost.days > 0:
    print(f"Осталось: {ost.days} дней")
  else:
    print(f"Прошло: {abs(ost.days)} дней")
ostatok(your_date)


#Задание 7
# Сделайте функцию, которая будет возвращать сколько дней осталось до конца текущего месяца.
import datetime as dt
print("Задача 7")
def ostatok ():
  current = dt.datetime.now()
  if current.month in (1, 3, 5, 7, 8, 10, 12):
    end_day =  31
  elif current.month == 2:
    end_day = 28
  else:
    end_day = 30
  ost = end_day - current.day
  print(f'До конца месяца осталось: {ost} дней')
ostatok()

#Задание 8
# Сделайте функцию, которая заполнит список N случайными числами из заданного промежутка.
import random
print("Задача 8")
inp = input("Введите через запятую: начало промежутка, конец промежутка, кол-во чисел:").split(",")
def random_list(start, stop, count_number):
  ls = [random.randint(int(start), int(stop)) for i in range(int(count_number))]
  print(ls)
random_list(inp[0],inp[1], inp[2])

# Задание 9
# Дан список событий за определенные месяцы, хранящийся в следующей структуре:
print("Задача 9")

events = [
    {
    'date': '2019-12',
    'event': 'name1'
    },
    {
    'date': '2019-12',
    'event': 'name2'
    },
    {
    'date': '2019-11',
    'event': 'name3'
    },
    {
    'date': '2019-11',
    'event': 'name4'
    },
    {
    'date': '2020-10',
    'event': 'name5'
    },
    {
    'date': '2020-10',
    'event': 'name6'
    },
    {
    'date': '2020-11',
    'event': 'name5'
    },
    {
    'date': '2020-11',
    'event': 'name6'
    },
    {
    'date': '2020-12',
    'event': 'name7'
    },
    {
    'date': '2020-12',
    'event': 'name8'
    },
    {'date': '2020-12',
    'event': 'name9'
    },
]
result = {}
for i in events:
    year, month = i['date'].split('-')
    if year not in result:
        result[year] = {}
    if month not in result[year]:
        result[year][month] = []
    result[year][month].append(i['event'])
print(result)

#Задание 10
# Дан такой словарь со списком дел за определенную дату, нужно вывести на экран все дела за 2018 г
print("Задача 10")
from datetime import datetime as dt
affairs = {
'2019-12-31': ['список дел'],
'2018-11-29': ['список дел'],
'2018-11-30': ['список дел'],
'2018-12-27': ['список дел'],
'2019-12-29': ['список дел'],
'2019-12-30': ['список дел'],
'2018-12-30': ['список дел'],
'2018-12-31': ['список дел'],
}
affairs_2018 = []

for date, tasks in affairs.items():
    if date.startswith('2018'):
        affairs_2018.extend(tasks)
print(affairs_2018)

# Задание 11
# Дан произвольный двумерный список необходимо получить список элементов главной диагонали
print("Задача 11")
import numpy as np
massive  = [
[11, 12, 13, 14, 15],
[21, 22, 23, 24, 25],
[31, 32, 33, 34, 35],
[41, 42, 43, 44, 45],
[51, 52, 53, 54, 55],
]
diagonal = []
matrix = np.array(massive)
shape = (np.shape(matrix))
for i in range(shape[0]):
    diagonal.append(matrix[i,i])
print(diagonal)

# Задание 12
# Дан URL необходимо получить из него набор папок
print("Задача 12")

url = 'http://test.com/dir1/dir2/dir3/page.html';
path = url.split('://')[1].split('/', 1)[1]

directories = path.split('/')[:-1]  # Убираем последний элемент (page.html)

# Формирование списка папок
result = []
current_path = ''
for i in directories:
    current_path += '/' + i
    result.append(current_path + '/')

print(list(reversed(result)))

# Задание 13
# Сделайте функцию, которая будет устанавливать правильную форму существительного после числа.
print("Задача 13")
a = input("Введите кол-во яблок:")

def nouns (count):
    if int(count) <= 20:
        if int(count) == 1:
            print(f"{count} яблоко")
        elif 1<int(count)<5:
            print(f"{count} яблока")
        elif 5<=int(count)<20:
            print(f"{count} яблок")
    elif int(count) > 20:
        if int(count[-1]) == 0:
            print(f"{count} яблок")
        elif int(count[-1])==1:
            print(f"{count} яблоко")
        elif 1<int(count[-1])<5:
            print(f"{count} яблока")
        elif int(count[-1]) <= 5:
            print(f"{count} яблок")

nouns(a)

# Задание 14
# Даны два числа. Выведите в консоль процесс умножения этих чисел в столбик, как в школе.
print("Задача 14")
a = int(input("Введите первое число для умножения: "))
c = int(input("Введите второе число для умножения: "))
def multiplication(num1, num2):
    num1_str = str(num1)
    num2_str = str(num2)

    intermediate_results = []
    for i, digit in enumerate(reversed(num2_str)):
        product = num1 * int(digit)
        intermediate_results.append(f"{product}{' ' * i}")

    print(f"  {num1}")
    print("x")
    print(f"  {num2}")
    print("-" * (len(num1_str) + 2 + len(num2_str)))
    print("+")

    for res in reversed(intermediate_results):
        print(f"  {res}")

    total = num1 * num2
    print("-" * (len(num1_str) + 2 + len(num2_str)))
    print(f" {total}")


multiplication(a, c)

#Задание 15
#Процесс деления
print("Задача 15")
dividend = int(input("Введите число которое нужно поделить: "))
divisor = int(input("Ведите делитель: "))
def division_process(dividend, divisor):
    dividend_str = str(dividend)
    divisor_str = str(divisor)

    current = ""
    index = 0
    result = ""
    remainder = 0

    print(f"{dividend_str} | {divisor_str}")
    print("-" * (len(dividend_str) + 1) + f"| {dividend // divisor}")

    while index < len(dividend_str):
        current += dividend_str[index]
        index += 1

        if int(current) < divisor:
            result += "0"
            if index == len(dividend_str):
                break
            continue

        quotient = int(current) // divisor
        remainder = int(current) % divisor
        result += str(quotient)
        if index == len(dividend_str):
            spaces = ""
        else:
            spaces = " " * (index - len(str(current)) - 1)

        print(f"{spaces}{str(current)}")
        print(f"{spaces}{str(quotient * divisor)}")
        print(f"{spaces}{'-' * len(str(quotient * divisor))}")

        current = str(remainder) + (dividend_str[index] if index < len(dividend_str) else "")

    print(" " * (len(dividend_str) - len(result)) + str(remainder))
division_process(dividend, divisor)

#Задание 16
#Разложение числа на множители
print("Задача 16")
def print_prime_factors(n):
    original_n = n
    print(f"Разложение числа {original_n} на простые множители:")
    while n % 2 == 0:
        print(f"{n} | 2")
        n //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            print(f"{n} | {i}")
            n //= i

    if n > 2:
        print(f"{n} | {n}")

number = int(input("Введите число для разложения на простые множители: "))
print_prime_factors(number)

# Задание 17
# Найти корни
print("Задача 17")
def find_roots(a, b, c):
    D = b ** 2 - 4 * a * c

    if D > 0:
        root1 = (-b + D ** 0.5) / (2 * a)
        root2 = (-b - D ** 0.5) / (2 * a)
        return (root1, root2)
    elif D == 0:
        root = -b / (2 * a)
        return (root,)
    else:
        return None


a = float(input("Введите коэффициент a (не равен 0): "))
while a == 0:
    a = float(input("Коэффициент a не может быть равен 0. Пожалуйста, введите значение снова: "))

b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

roots = find_roots(a, b, c)

if roots is None:
    print(f"Уравнение {a}x^2 + {b}x + {c} = 0 не имеет действительных корней.")
elif len(roots) == 1:
    print(f"Уравнение {a}x^2 + {b}x + {c} = 0 имеет один корень: {roots[0]}")
else:
    print(f"Уравнение {a}x^2 + {b}x + {c} = 0 имеет два корня: {roots[0]} и {roots[1]}")


# Задание 18
# Генерация пароля
print("Задача 18")
import random
import string


def generate_password(length):
    if length < 4:
        raise ValueError("Длина пароля должна быть не менее 4 символов.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    all_characters = lowercase + uppercase + digits + special_characters
    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)

    return ''.join(password)

password_length = int(input("Введите длину пароля (минимум 4): "))
try:
    generated_password = generate_password(password_length)
    print(f"Сгенерированный пароль: {generated_password}")
except ValueError as e:
    print(e)

# Задача 19
# Проверка сложности пароля
print("Задача 19")


def check_password(password):
    length_criteria = len(password) >= 8
    lowercase_criteria = any(i.islower() for i in password)
    uppercase_criteria = any(i.isupper() for i in password)
    digit_criteria = any(i.isdigit() for i in password)
    special_char_criteria = any(i in '!@#$%^&*()-_=+[]{}|;:,.<>?/' for i in password)

    criteria_met = [
        length_criteria,
        lowercase_criteria,
        uppercase_criteria,
        digit_criteria,
        special_char_criteria
    ]

    complexity_score = sum(criteria_met)

    if complexity_score == 5:
        return "Пароль очень сильный."
    elif complexity_score == 4:
        return "Пароль сильный."
    elif complexity_score == 3:
        return "Пароль средний."
    else:
        return "Пароль слабый."

user_password = input("Введите пароль для проверки сложности: ")
complexity_result = check_password(user_password)
print(complexity_result)


# Задача 20
# Алгоритм Эратосфена
print("Задача 20")
def eratosphene (start, end):
    if end < 2:
        return []
    if start < 2:
        start = 2

    is_prime = [True] * (end + 1)
    is_prime[0] = is_prime[1] = False

    for number in range(2, int(end**0.5) + 1):
        if is_prime[number]:
            for multiple in range(number * number, end + 1, number):
                is_prime[multiple] = False

    primes = [num for num in range(start, end + 1) if is_prime[num]]
    return primes

start = int(input("Введите нижний предел: "))
end = int(input("Введите верхний предел: "))

prime_numbers = eratosphene(start, end)
print(f"Простые числа в диапазоне от {start} до {end}: {prime_numbers}")