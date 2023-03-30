n = int(input("Введите число: "))
string = int(input("Введите последовательность: "))
my_nums = []
print(string)
my_nums.extend(string)
my_nums.insert(0, n)
my_nums.sort(reverse=True)
print(my_nums)
10

# def f(n):
#     if n == 0:
#         return ''
#     k = int(input())
#     return f(n-1)+f'{k}'


# n = int(input())
# print(f(n))
