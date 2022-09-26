# def same_by(characteristic, object):
#     list_1 = [characteristic(el) for el in object]
#     return len(object) == list_1.count(0)

def same_by(characteristic, object):
    return len(object) == [characteristic(el) for el in object].count(0)
values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')



