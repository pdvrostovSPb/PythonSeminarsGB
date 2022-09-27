# Задача: Создать калькулятор для работы с рациональными и комплексными числами, 
# организовать меню, добавив в неё систему логирования.

# https://github.com/Naganishe/Calc-Seminar7.git репозиторий 2 зала 7 семинара


from math import pi

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
lst = [list(i) for i in orbits]
square_lst = []
for i in range(len(lst)):
    for j in range(len(lst[i]) - 1):
        if lst[i][j] == lst[i][j + 1]: continue
        sq = lst[i][j] * lst[i][j + 1] * pi
        square_lst.append(sq)
    print(square_lst)
max_sq = max(square_lst)
index = square_lst.index(max_sq)
print(orbits[index])