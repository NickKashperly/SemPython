a = int(input("Введите число:"))
factorial = 1
while a > 1:
    factorial *= a
    a -= 1
print(f"Факториал = {factorial}")
