# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

try:
    quater_number = int(input('Введите номер четверти: '))
    if (0 < quater_number < 5) == False:
        print('Некорректный ввод. Введите номер от 1 до 4.')
    elif quater_number == 1:
        print('Диапазон возможных координат: x > 0; y > 0')
    elif quater_number == 2:
        print('Диапазон возможных координат: x < 0; y > 0')
    elif quater_number == 3:
        print('Диапазон возможных координат: x < 0; y < 0')
    else:
        print('Диапазон возможных координат: x > 0; y < 0')
except:
    print('Некорректный ввод')

