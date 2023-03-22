import math
x = int(input("Введите сумму чисел: "))
y = int(input("Введите произведение чисел: "))
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print('Это числа: ', i, j)


# s = int(input("Введите сумму: "))
# p = int(input("Введите произведение: "))

# b = (s + math.sqrt(s**2 - 4*p)) / 2
# a = s - b

# print(f"{int(a)} {int(b)}")


# s = int(input("Сумма чисел X и Y: "))
# p = int(input("Произведение чисел X и Y: "))

# for x in range(1, 1001):
#     if p % x == 0:
#         y = int(p / x)
#         if y == s - x:
#             print(x, y)
# else:
#     print("Решения нет")