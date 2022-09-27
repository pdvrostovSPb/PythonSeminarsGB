# Самая далекая планета
from math import pi

def max_square_index(x: list)-> int:
    '''
    функция, получающая на вход список кортежей с длинами полуосей эллипсов
    и возвращающая индекс кортежа с данными самого большого по площади эллипса
    '''
    square_lst = []
    for i in range(len(x)):
        for j in range(len(x[i]) - 1):
            if x[i][j] == x[i][j + 1]: continue
            square_lst.append(x[i][j] * x[i][j + 1] * pi)
    return square_lst.index(max(square_lst))

def find_farthest_orbit(list_of_orbits)-> tuple:
    '''
    Функция возвращающая из списка кортеж с длинами полуосей эллипса
    с самой большой площадью
    '''
    return list_of_orbits[max_square_index(list_of_orbits)]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))





