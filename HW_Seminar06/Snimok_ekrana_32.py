def operation_table(func, row=9, columns=9):
    '''
    функция, позволяющая выводить таблицы умножения, сложения, возведения
    в степень и т.д., за счет изменения аргумента, который является более
    простой функцией
    '''
    for i in range(1, row + 1):
        for j in range(1, columns + 1):
            print(f'{func(i, j)}', end=' \t')
        print()

operation_table(lambda x, y: x * y, 4)
print()
operation_table(lambda x, y: x + y, 5)
print()
operation_table(lambda x, y: x ** y, 6)
