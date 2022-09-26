# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.

# Входные данные
# В первой строке входного файла INPUT.TXT
# записано натуральное число N (1 ≤ N ≤ 100) – число монеток.
# В каждой из последующих N строк содержится одно целое число
# 1 если монетка лежит решкой вверх и 0 если вверх гербом.

# Выходные данные
# В выходной файл OUTPUT.TXT выведите минимальное количество монет, которые нужно перевернуть.

data_entry = []
for i in open('input_coins.txt'):
    data_entry.append(i[:-1])

number_of_tails = 0
# for i in range(1, len(data_entry)):
#     if int(data_entry[i]):
#         number_of_tails += 1


with open('output_coins.txt', 'w') as data_output:
    if number_of_tails < int(data_entry[0]) / 2:
        data_output.write(str(number_of_tails))
    else:
        data_output.write(str(int(data_entry[0]) - number_of_tails))
