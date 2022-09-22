# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


from re import L


def reading_file(name:str) -> str:
    '''
    чтение файла
    reading a file
    '''
    with open(name, 'r') as f:
        read_data = f.read()
        return read_data


#print(reading_file('input_rle.txt'))
read_data = list(reading_file('input_rle.txt'))
# lst = list(read_data)
print(read_data)

def compression(str:str) -> str:
    '''
    модуль сжатия
    compression module
    '''
    compressed_str = ''

    for i in range(1, len(str)):
        counter = 1 # счетчик одинаковых элементов строки
                 
        
        
        
        while i < len(str) and str[i] == str[i + 1]:
            counter += 1
            i += 1
        if str[i] == str[i - 1]: continue
            
        compressed_str = compressed_str + str(counter) + str[i]     

    return compressed_str

print(compression(read_data))          
                
        










