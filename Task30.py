def f(a, d, n):
    if n == 0:
        return list_1.sort(reverse=False)
    c = a+(n-1)*d
    list_1.append(c)
    return f(a, d, n-1)


list_1 = []

a = int(input('Введите первое число: '))
d = int(input('Введите разность чисел: '))
n = int(input('Введите количество чисел: '))

f(a, d, n)
print(*list_1)


# a1 = int(input())
# d = int(input())
# n = int(input())
# for i in range(n):
#     print(a1 + i * d)
