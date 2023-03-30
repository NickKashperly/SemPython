number = int(input("Введите число: "))
list_score = []
for i in range(number):
    if number % (i+1) == 0:
        list_score.append(i)
print(*list_score)
if len(list_score) <= 2:
    print("Число простое!")
else:
    print("Число не простое!")
