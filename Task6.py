num = int(input("Введите шестизначный номер билета: "))
a = num//100 % 10
b = num//10 % 10
c = num % 10
sum1 = a+b+c
d = num//1000 % 10
e = num//10000 % 10
f = num//100000
sum2 = d+e+f
if sum1 == sum2:
    print("У Вас СЧАСТЛИВЫЙ билет!!!")
else:
    print("У Вас обычный билет.")


# n = input()
# if int(n[0]) + int(n[1]) + int(n[2]) == int(n[3]) + int(n[4]) + int(n[5]):
#     print('yes')
# else:
#     print('no')
