# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Введите число: n = '))
binary_number = ''
while n / 2 > 0:
    binary_number = str(n % 2) + binary_number
    n //= 2
print(binary_number)
