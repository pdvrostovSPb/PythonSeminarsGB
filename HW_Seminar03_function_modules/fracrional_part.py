# Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

real_numbers = [1.11, 3.33, 10.00]
for i in range(len(real_numbers)):
    real_numbers[i] = real_numbers[i] - round(real_numbers[i])
print(round(max(real_numbers) - min(real_numbers), 2)) 

