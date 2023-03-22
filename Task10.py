from random import randint

n_user = int(input("Введите количество монет:"))
eagle = 0
tails = 0
min_coin = 0

for i in range(n_user):
    coin = randint(0, 1)
    print(coin, end=" ")
    if coin == 0:
        eagle += 1
    else:
        tails += 1
if eagle >= tails:
    min_coin = tails
else:
    min_coin = eagle

print(
    f"\nМинимальное количество монет которые нужно перевернуть:  {min_coin} ")
