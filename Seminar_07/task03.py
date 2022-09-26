def operation_table(func, row=9, columns=9):
    for i in range(row):
        for j in range(columns):
            print(f'{func(i + 1, j + 1)}', end=' \t')
        print()


operation_table(lambda x, y: x * y, 5)
