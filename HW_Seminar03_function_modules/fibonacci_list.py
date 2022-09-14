# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.(Доп)
# Пример:

# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

n = int(input("Введите число n = "))
list = []
for i in range(1, n + 1):
    list.append(fib(i))

list_0 = [0]
list_1 = list.copy()
list.reverse()

for i in range(0, n - 1, 2):
    if not len(list) % 2:
        list[i] = int(list[i]) * -1
    else:
        list[i + 1] = int(list[i + 1]) * -1

print(list + list_0 + list_1)



    