# Создать функцию, которая принимает от пользователя номер месяца и говорит, к какому сезону месяц принадлежит. Решать через словари, if else, функции.
def start():
    a = int(input("Choose a month by number:\n"))
    if a == 1 or a == 2 or a == 12:
        print("Winter")
    elif a == 3 or a == 4 or a == 5:
        print("Spring")
    elif a == 6 or a == 7 or a == 8:
        print("Summer")
    elif a == 9 or a == 10 or a == 11:
        print("Autumn")
    else:
        print("Invalid number!")
    return a


