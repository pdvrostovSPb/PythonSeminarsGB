# 35. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

polinom_1 = open('input_01_polin.txt', 'r')
print(polinom_1.read().split(' '))
polinom_1.close()
polinom_2 = open('input_02_polin.txt', 'r')
print(polinom_2.read().split(' '))
polinom_2.close()