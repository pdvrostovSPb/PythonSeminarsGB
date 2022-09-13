# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

data_entry = [2, 8, 5, 6, 30, 1, 4, 5, 1]
len_data_entry = 0
if not len(data_entry) % 2:
    len_data_entry = len(data_entry) / 2
else:
    len_data_entry = len(data_entry) / 2 + 1
for i in range(int(len_data_entry)):
    print((data_entry[i] * data_entry[len(data_entry) - 1 - i]), end=' ')