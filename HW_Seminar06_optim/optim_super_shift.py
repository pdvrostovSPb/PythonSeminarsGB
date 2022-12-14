# Суперсдвиг
# (Время: 1 сек. Память: 16 Мб Сложность: 20%)
# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на |K| элементов вправо, если K – положительное и влево, если отрицательное.

# Входные данные
# Первая строка входного файла INPUT.TXT содержит натуральное число N,
# во второй строке записаны N целых чисел Ai,
# а в последней – целое число K. (1 ≤ N ≤ 105, |K| ≤ 105, |Ai| ≤ 100).
# Выходные данные
# В выходной файл OUTPUT.TXT выведите полученную последовательность.

from random import randint


try:
    n = int(input('Введите число N от 1 до 105: N = '))
    k = int(input('Введите число сдвига K от -105 до 105: K = '))
    list = [randint(-100, 100) for i in range(n)] # list comprehension
    print(list) # вывод для наглядной проверки последующего ответа
    print(list[(n - k % n):n] + list[:(n - k % n)]) 
except:
    print('Некорректный ввод')