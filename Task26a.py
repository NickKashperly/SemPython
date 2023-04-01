

def palindrom(a):
    if len(a) <= 1:
        return print('Это палиндром!')
    elif a[0] == a[len(a)-1]:
        palindrom(a[1:len(a) - 1])

    else:
        return print('Это не палиндром!')


a = input("Введите текст: ")


palindrom(a)
