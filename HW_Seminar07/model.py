def input_data(file: str) -> list:
    '''

    '''
    with open(f'{file}', 'r', encoding="utf-8") as f:
        data = f.readlines()
    return data

print(input_data('input_phonebook.txt'))

def valid_data(values: list) -> list:
    
    pass

def output_data():
    pass

