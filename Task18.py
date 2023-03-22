from random import randint
a = []
n = int(input("Введите количество числе в списке:  "))
x = int(input("Искомое число:  "))
for i in range(n):
    a.append(randint(1,10))
print(a)
j = 0
find_res = 0
flag = True
while find_res == 0:
    i = 0
    while i<n and flag:
        if abs(x-a[i])==j:
            find_res = a[i]
            flag = False
        i+=1
    j+=1

print(f'res = {find_res}')