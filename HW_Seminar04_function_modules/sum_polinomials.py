# 35. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

data_entry = open('input_01_polin.txt', 'r')
polinom_1 = data_entry.read().split(' ')
data_entry.close()
data_entry = open('input_02_polin.txt', 'r')
polinom_2 = data_entry.read().split(' ')
data_entry.close()
print(polinom_1)
print(polinom_2)
sum = polinom_1 + polinom_2
print(sum)
sum_item = 0
for item in sum:
    for e in item:
        if e.find('x'):
            
            print(e)

    #     sum_item = sum_item + int(item)
    #     del(item)

