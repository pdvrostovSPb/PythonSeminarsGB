# Оптимизированный вариант решения

def viny_song(song):
    vowels = ["а", "я", "у", "ю", "о", "е", "ё", "э", "и", "ы"]
    lst = [len(list(filter(lambda x: x in vowels,i))) for i in song.split()]
    return ('Пам парам','Парам пам-пам')[len(set(lst)) == 1]

song = 'если урок идет рано то-ли'
print(viny_song(song))