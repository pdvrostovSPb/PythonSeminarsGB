def same_by(characteristic, object):
    '''
    Проверяем на истинность, все ли объекты имеют одинаковое значение какой-либо характеристики
    '''
    return len(object) == [characteristic(i) for i in object].count(0)

values = [0, 2, 10, 6]

# проверяем на истинность четность элементов

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')