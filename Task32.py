from random import randint
garden_bed_list = []
n = int(input("Введите количество элементов массива:  "))
for i in range(n):
    garden_bed_list.append(randint(-10, 10))
print(garden_bed_list)
a = int(input("Введите начало диапозона от -10 до 10: "))
b = int(input("Введите конец диапозона от  a до 10: "))
list_1 = []
for i in range(n):
    if a < garden_bed_list[i] < b:
        list_1.append(i)
print("Числа в указанном диапозоне находятся на позициях : ", *list_1)


# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list_1)):
#     if min_number <= list_1[i] <= max_number:
#         print(i)
