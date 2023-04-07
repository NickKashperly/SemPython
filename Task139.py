# Два различных натуральных числа n и m называются дружественными,
# если сумма делителей числа n (включая 1, но исключая само n) равна
# числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое
# из которых не превосходит k. Программа получает на вход одно натуральное
# число k, не превосходящее 105. Программа должна вывести все пары дружественных чисел,
# каждое из которых не превосходит k. Пары необходимо выводить по одной в строке,
# разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).


import sys
sys.setrecursionlimit(100000)


k = int(input("Введите число: "))


def friend(k):
    if k <= 1:
        return " "
    else:
        count_1 = 0
        count_2 = 0
        for i in range(1, k-1):
            if k % i == 0:
                count_1 += i
                # print(1, count_1)
            else:
                i += 1

        for j in range(1, count_1-1):
            if count_1 % j == 0:
                count_2 += j
                # print(2, count_2)
            else:
                j += 1

        if k == count_2 and k < count_1:
            print(k, count_1, "Числа побратимы")
        return friend(k-1)


friend(k)


# def multRange(start, end):
#     if start >= end - 1:
#         return start
#     mid = (start + end) // 2
#     return multRange(start, mid) * multRange(mid, end)

# # вычисление n! рекурсией


# def factRec(n): return 1 if n < 2 else multRange(2, n + 1)


# print(factRec(20000))
