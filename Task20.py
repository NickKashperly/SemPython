dict = {1: 'AEIOULNSTR АВЕИНОРСТ',
        2: 'DG ДКЛМПУ',
        3: 'BCMP БГЁЬЯ',
        4: 'FHVWY ЙЫ',
        5: 'K ЖЗХЦЧ',
        8: 'JZ ШЭЮ',
        10: 'QZ ФЩЪ'}

word = input('Введите слово:').upper()
count = 0
for i in word:
    for v in dict:
        if i in dict[v]:
            count += v
print('За это слово вы получаете', count, 'очков')


# dict_2 = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8,
#           "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10,
#           'А': 1, 'Б': 3, 'В': 1, 'Г': 3, 'Д': 2, 'Е': 1, 'Ё': 3, 'Ж': 5, 'З': 5, 'И': 1,
#           'Й': 4, 'К': 2, 'Л': 2, 'М': 2, 'Н': 1, 'О': 1, 'П': 2, 'Р': 1, 'С': 1, 'Т': 1, 'У': 2, 'Ф': 10,
#           'Х': 8, 'Ц': 5, 'Ч': 5, 'Ш': 8, 'Щ': 10, 'Ъ': 10, 'Ы': 4, 'Ь': 3, 'Э': 8, 'Ю': 8, 'Я': 3}

# word = str.upper(input("Введите слово: "))

# score = 0
# for letter in word:
#     score = score + dict_2[letter]

# print(f'Введенное слово {word} получает в игре {score} очков(-а)')

"""
def HowMuchScore(char):
    # создаем словарь, где ключ - стоиость, а значение - символы имеющие дданную стоимость
    dictionary = {1: "AEIOULNSTRАВЕИНОРСТ", 2: "DGДКЛМПУ",
                  3: "BCMPБГЁЬЯ", 4: "FHVWYЙЫ", 5: "KЖЗХЦЧ", 8: "JXШЭЮ", 10: "QZФЩЪ"}
    i = 1
    while i < 11:  # цикл пока не пройдем все ключи в словаре
        # пытаемся получить значение по ключу, если такой ключ отсутствует (например 6, 7) то возвращаем 0
        data = dictionary.get(i, 0)
        if data != 0:  # если значение получено
            if char in data:  # проверяем есть ли интересующий нас символ в слове-значении из словаря
                return i  # если есть - возвращаем стоимость
        i = i+1
    return 0  # тут мы окажемся, если запрашиваемый символ отсутствет в словаре, тогда возвращаем 0


# запрашиваем слово у пользователя и сразу переводим его в верхний регистр
word = str.upper(input("Введите слово для оценки:"))

score = 0  # переменная для подсчета стоимости слова

for i in word:
    # проходим по символам в слове, узнавая их стоимость и суммируем в результат
    score = score+HowMuchScore(i)

print(f"Стоимость слова {score} баллов")  # выводим результат

"""