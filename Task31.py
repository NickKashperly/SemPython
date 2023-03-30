def fib(n):
    if n in [1, 2]:
        return 1
    print(n)
    return fib(n-1)+fib(n-2)


n = int(input("Введите число N: "))
print(fib(n))
