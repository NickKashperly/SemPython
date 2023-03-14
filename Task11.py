a = int(input("Введите положительное число: "))
count = 3
fibonachi = -1
c = 1
d = 1
while fibonachi < a:
    fibonachi = c + d
    c = d
    d = fibonachi
    count += 1

if fibonachi == a:
    print(count)
else:
    print(-1)
