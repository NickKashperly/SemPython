def f(n, list_1):
    if n == 0:
        return list_1
    k = int(input())
    list_1.append(k)
    return f(n-1, list_1)


list_1 = []

n = int(input())
print(f(n, list_1))


def list_3(list_1):
    count = 0
    for i in range(2, len(list_1)):
        if list_1[i-2] < list_1[i-1] > list_1[i]:
            count = count + 1
    return count


print(list_3(list_1))
