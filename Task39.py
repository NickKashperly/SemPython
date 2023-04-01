def f(n, list_1):
    if n == 0:
        return list_1
    k = int(input())
    list_1.append(k)
    return f(n-1, list_1)


list_1 = []
list_2 = []
n = int(input())
print(f(n, list_1))
n = int(input())
print(f(n, list_2))


def list_3(list_1, list_2):
    new_list = []
    for element in list_1:
        for k in range(len(list_2)):
            if list_2[k] !=
