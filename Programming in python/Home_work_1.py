import math

# -------------Exercise 1
# n = int(input())
# Sum = (n * (n + 1)) / 2
# print(f'Сумма первых положительных чисел равна {Sum}')

# ------------Exercise 2
# x1 = int(input())
# x2 = int(input())
# print(f'Результат сложения {x1 + x2}')
# print(f'Результат вычитания {x1 - x2}')
# print(f'Результат умножения {x1 * x2}')
# print(f'Результат деления {round(x1 / x2, 2)}')
# print(f'Результат целочисленного деления {x1 // x2}')
# print(f'Остаток от деления {x1 % x2}')
# print(f'Результат возведения в степень {x1 ** x2}')
# print(f'Результат логорифма по основания 10 {round(math.log10(x1),), round(math.log10(x2),2)}')
# print(f'x1 < x2? {x1 < x2}')
# print(f'x1 <= x2? {x1 <= x2}')
# print(f'x1 > x2? {x1 > x2}')
# print(f'x1 >= x2? {x1 >= x2}')
# print(f'x1 != x2? {x1 != x2}')
# print(f'x1 == x2? {x1 == x2}')

# ------------------Exercise 3
# x = int(input())
# y = int(input())
# z = int(input())
# f = (math.pow(((x ** 5 + 7) / (abs(-6) * y)), 1 / 3)) / (7 - z * (abs(y)))
# print(f'Значение выражения {round(f, 3)}')

# -------------------Exercise 4
# R1 = float(input())
# R2 = float(input())
# R = R1 + R2
# print(f'Общее сопротивление {round(R,1)}')

# -------------------Exercise 5
# a = int(input())
# b = int(input())
# m = int(input())
# n = int(input())
# x = -b / a
# if m < x < n:
#     print('Да')
# else:
#     print('Нет')

# -----------------Exercise 6
v = int(input())
t = int(input())
dist = (((v * t) / 123) - ((v * t) // 123)) * 123
print(f'Спортсмен остановился на {int(dist)} киллометре')
