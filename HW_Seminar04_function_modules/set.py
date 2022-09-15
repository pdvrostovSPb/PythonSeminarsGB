# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

list = [2, 45, 7, 6, 2, 12, 45, 1]
set_list = []

for i in range(len(list)):
    flag = False
    for j in range(len(list)):
        if i == j:
            continue
        if list[i] == list[j]:
            flag = True
    if flag == False:
        set_list.append(list[i])
print(set_list)


