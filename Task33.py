from random import randint
n = int(input("Введите количество оценок: "))
list_score = []
minimal_score = 5
maximum_score = 0
pouz_maximal = []
for i in range(n):
    list_score.append(randint(1, 5))
print(list_score)
for i in range(n):
    if minimal_score > list_score[i]:
        minimal_score = list_score[i]
    elif maximum_score < list_score[i]:
        maximum_score = list_score[i]
        pouz_maximal.clear()
        pouz_maximal.append(i)
        print(pouz_maximal)
    elif maximum_score == list_score[i]:
        pouz_maximal.append(i)
        print(pouz_maximal)
for k in range(n):
    for j in range(len(pouz_maximal)):
        if k == pouz_maximal[j]:
            list_score[k] = minimal_score
print(*list_score)
