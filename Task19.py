# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

list_1 = [1, 2, 3, 4, 5]
list_2 = []

k = int(input("Введите число, на которое нужно сделать сдвиг: "))

for i in range(k):
    list_2.append(list_1[0])
    list_1.pop(0)
print(list_1+list_2)


# arr = [1, 2, 3, 4, 5]
# k = 3
# arr = arr[k:] + arr[:k]
# print(arr)


# lst = [1, 2, 3, 4, 5]
# k = 2
# for i in range(k):
#     lst.insert(0, lst.pop(-1))
# print(lst)
