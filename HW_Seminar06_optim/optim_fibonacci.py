# Требуется найти N-е число Фибоначчи.
# Входные данные
# Во входном файле INPUT.TXT записано целое число N (0 ≤ N ≤ 30).
# Выходные данные
# В выходной файл OUTPUT.TXT выведите N-е число Фибоначчи.

def current_num(first: int, second: int, fib: int, n: int)-> int:
    '''
    Вычисляем значение числа Фибоначчи по заданному порядковому номеру
    '''
    for i in range(n):
        first = fib
        fib = first + second
        second = first
    return fib 

with open('input_fibonacci.txt', 'w') as data_entry: # создаем файл
    data_entry.write('10') # записываем целое число N (0 ≤ N ≤ 30)

with open('input_fibonacci.txt', 'r') as reading_data: # открываем файл 
    N = int(reading_data.read()) # считываем и присваиваем целочисленное N

first_number = 0
second_number = 1
fibonacci_number = 0
fibonacci_number = current_num(first_number, second_number, fibonacci_number, N)
    
with open('output_fibonacci.txt', 'w') as data_output: # создаем файл output_fibonacci.txt 
    data_output.write(str(fibonacci_number)) # записываем значения N-го числа Фибоначчи