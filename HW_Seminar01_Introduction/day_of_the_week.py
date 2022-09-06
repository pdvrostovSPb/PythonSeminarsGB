# Напишите программу, которая принимает на вход цифру,
#  обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

try:
    day_of_the_week = int(input('Введите номер дня недели от 1 до 7 '))
    if day_of_the_week == 6 or day_of_the_week == 7:
        print('да')
    elif day_of_the_week >= 1 and day_of_the_week <= 5:
        print('Нет')
    else:
        print('Некорректный ввод')

except:
    print('Некорректный ввод')


