from random import randint
first_set = set()
second_set = set()
n = int(input("Введите количество числе в первом наборе:  "))
m = int(input("Введите количество числе во втором наборе:  "))
for i in range(n):
    first_set.add(randint(1, 100))
print(first_set)
for i in range(m):
    second_set.add(randint(1, 100))
print(second_set)
intersection_list = list(first_set.intersection(second_set))
intersection_list.sort()
print(*intersection_list)

# j = 0
# find_res = 0
# flag = True
# while find_res == 0:
#     i = 0
#     while i < n and flag:
#         if abs(x-a[i]) == j:
#             find_res = a[i]
#             flag = False
#         i += 1
#     j += 1

# print(f'res = {find_res}')
