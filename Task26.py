#  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.


def f(a, b):
    if b == 0:
        return 1
    return a*f(a, b-1)


a = int(input("Введите число А: "))
b = int(input("Введите число В: "))
print(f(a, b))
