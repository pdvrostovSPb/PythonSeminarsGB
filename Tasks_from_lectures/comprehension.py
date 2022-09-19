# выбрать из списка четные и сотавить список пар чисел и их кубов


with open('input_compr.txt', 'r') as data_entry:
    list = list(map(int, data_entry.read().split(' ')))
print(list)
list_1 = [(i, i ** 3) for i in list if i%2 == 0]
print(list_1)


# lst = [x for x in range(1, 21)]
# print(lst)
# lst = list(map(lambda x: x + 10, lst))
# print(lst)
