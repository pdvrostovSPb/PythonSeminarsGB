# Требуется найти N-е число Фибоначчи.
# Входные данные
# Во входном файле INPUT.TXT записано целое число N (0 ≤ N ≤ 30).
# Выходные данные
# В выходной файл OUTPUT.TXT выведите N-е число Фибоначчи.




with open('input_fibonacci.txt', 'w') as data_entry: # создаем файл
    data_entry.write('7') # записываем целое число N (0 ≤ N ≤ 30)

with open('input_fibonacci.txt', 'r') as reading_data: # открываем файл 
    N = int(reading_data.read()) # считываем и присваиваем целочисленное N

fibonacci_number = 0
second_number = 1
for i in range(N):
    first_number = fibonacci_number
    fibonacci_number = first_number + second_number
    second_number = first_number
    
with open('output_fibonacci.txt', 'w') as data_output: # создаем файл output_fibonacci.txt 
    data_output.write(str(fibonacci_number)) # записываем значения N-го числа Фибоначчи