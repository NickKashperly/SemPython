# Задача 38: Дополнить телефонный справочник возможностью
# изменения и удаления данных. Пользователь также может
# ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных
def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии и изменить данные\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справичник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input())
    return choice


def show_menu2() -> int:
    print("Выберите необходимое действие\n"
          "1. Удалить абонента\n"
          "2. Изменить Фамилию\n"
          "3. Изменить Имя\n"
          "4. Изменить Номер телефона\n"
          "5. Изменить Описание\n"
          "6. Выйти в главное меню")
    choise = int(input())
    return choise


def read_csv(filename: str):
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(",")))
            data.append(record)
        return data


def print_resalt(data: list):
    print()
    print()
    for el in data:
        for k, v in el.items():
            print(f'{k}: {v}')
        print()
    # input("Для продолжения нажмите клавишу Enter")


def find_abonent_family(data):
    family = input("Введите фамилию абонента: ")
    count = 0
    index = 0
    find_abonent = []
    for el in data:
        if family in el["Фамилия"]:  # ищет частичное совпадение фамилии
            count += 1
            find_abonent.append(el)
            print(count, 'найденный абонент: ')
            for k, v in el.items():
                print(f'{k}: {v}')
            print()
        if count > 1:
            index = int(input('Найдено несколько абонентов\n'
                              'Если не хотите ничего делать нажмите 0\n'
                              "Если хотите изменить абонента, напишите номер найденого: "))
            if index > 0:
                count = 1
                index = index-1
                print()
        if count == 1:
            choise = 0
            while choise < 7:
                choise = show_menu2()
                if choise == 1:
                    data.remove(find_abonent[index])
                    print("Абонемент удален\n")
                if choise == 2:
                    find_abonent[index]["Фамилия"] = input(
                        'Введите новую Фамилию: ')
                    print("изменения внесены\n")
                if choise == 3:
                    find_abonent[index]['Имя'] = input(
                        "Введите новое Имя: ")
                    print('Изменения внесены\n')
                if choise == 4:
                    find_abonent[index]["Телефон"] = input(
                        "Введите новый номер телефона: ")
                    print('Изменения внесены\n')
                if choise == 5:
                    find_abonent[index]["Описание"] = input(
                        "Введите описание для абонента: ")
                    print("Изменения внесены\n")
                if choise == 6:

                    print("Вы вышли в главное меню")
                    show_menu()
                if choise >= 7:
                    print('Повторите команду\n')
        if count == 0:
            print("Указанная фамилия не найдена")
            print()


def find_abonent_number(data):
    number = input('Введите телефон абонента: ')
    count = 0
    find_number = []
    for el in data:
        if number in el['Телефон']:
            count += 1
            find_number.append(el)
            print(count, "Телефоны найденные")
            for k, v in el.items():
                print(f'{k}: {v}')
            print()
        if count == 0:
            print("Указанный номер не найден")
            print()


def add_abonent(data):
    list1 = []
    fields = ["Фамилия", 'Имя', "Телефон", "Описание"]
    list1.append(input("Введите Фамилию абонента: "))
    list1.append(input("Введите Имя абонента: "))
    list1.append(input("Введите Телефон абонента: "))
    list1.append(input("Введите Описание абонента: "))
    new_abonent = dict(zip(fields, list1))
    data.append(new_abonent)
    print()
    print('Вы добавили нового абонента: ')
    for k, v in new_abonent.items():
        print(f"{k},{v}")
    print()


def save_spravochnik(data):
    with open(input("Введите название файла: "), 'w', encoding="utf-8") as new_file:
        for i in data:
            str_1 = ""
            for v in i.values():
                str_1 += v+","

                str_1 = str_1[:-1]
                new_file.write(str_1 + "\n")
        print("Справочник сохранен")


spravochnik = read_csv("phonebook.csv")
choise = 0
while choise < 7:
    choise = show_menu()
    if choise == 1:
        print_resalt(spravochnik)
    if choise == 2:
        find_abonent_family(spravochnik)
    if choise == 3:
        find_abonent_number(spravochnik)
    if choise == 4:
        add_abonent(spravochnik)
    if choise == 5:
        save_spravochnik(spravochnik)
    if choise == 6:
        print("Приложение закрыто!")
        break
    if choise >= 7:
        print('Команда ненайдена!!! Повторите ввод')
        choise = 0
        show_menu()
