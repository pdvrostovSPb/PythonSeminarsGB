# Напишите программу, которая принимает на вход
# координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

try:
    x1 = round(float(input('Введите координату х1 = ')), 2)
    y1 = round(float(input('Введите координату y1 = ')), 2)
    x2 = round(float(input('Введите координату х2 = ')), 2)
    y2 = round(float(input('Введите координату y2 = ')), 2)


    distance_between_points = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(round(distance_between_points, 3))

except:
    print('Некорректный ввод')
