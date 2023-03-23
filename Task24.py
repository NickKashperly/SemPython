# from random import randint
# garden_bed_list = []
# sum = 0
# n = int(input("Введите количество кустов в грядке:  "))
# m = int(input("Введите номер куста перед которым находится собирающий модуль:  "))
# for i in range(n):
#     garden_bed_list.append(randint(30, 50))
# print(garden_bed_list)

# for i in range(m-3, m):
#     sum += garden_bed_list[i]
#     i += 1
# print(sum)

from random import randint
garden_bed_list = []
sum = 0
sum1 = 0
n = int(input("Введите количество кустов в грядке:  "))
for i in range(n):
    garden_bed_list.append(randint(30, 32))
print(garden_bed_list)

for i in range(n):
    for j in range(0, 3):
        sum1 += garden_bed_list[(i-j)]
        j += 1
        if sum1 > sum:
            sum = sum1
            nums = []
            nums.append(i+1)
        elif sum1 == sum:
            nums.append(i+1)
    sum1 = 0
    i += 1
print("Максимальное число ягод: ", sum,
      ", когда собирающий модуль находится перед кустами: ", *nums)
