# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


k = int(input('Введите степень многочлена: k = '))
coefficients = []
for i in range(k):
    if i != k - 1:
        coefficients.append(str(randint(0, 100)) + 'x' + '^' + str(k - i) + ' + ')
        print(coefficients[i], end='')
    else:
        coefficients.append(str(randint(0, 100)) + 'x' + '^' + str(k - i))
        print(coefficients[i], '+', randint(0, 100), '= 0')
