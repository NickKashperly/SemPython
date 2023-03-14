len1 = int(input("Введите количество долек по первой стороне: "))
len2 = int(input("Введите количество долек по второй стороне: "))
num = int(input("Введите количество долек которое вы хотите отломить:"))
s = len1*len2
if s > num and (num % len1 == 0 or num % len2 == 0):
    print('YES')
else:
    print('NO')
