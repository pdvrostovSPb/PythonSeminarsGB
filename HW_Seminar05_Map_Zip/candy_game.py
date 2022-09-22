# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока
# делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# 1 a
from random import randint as rd
from sys import exit


def check_win(m, n):
    if m == 1 and n == 0:
        return 'Выиграл бот'
    elif m == 0 and n == 0:
        return 'Выиграл пользователь'
    return None


j = 0 # 0 - ходит пользователь, 1 - ход бота
n = 29
while n > 0:
    if n >= 28:
        count_user = int(input("Сколько Вы хотите взять конфет?(от 1 до 28): "))
        while count_user < 1 or count_user > 28:
            count_user = int(input("Вы ошиблись, попробуйте заново\nСколько Вы хотите взять конфет?(от 1 до 28): "))
    else:
        count_user = int(input(f"Сколько Вы хотите взять конфет?(от 1 до {n}): "))
        while count_user < 1 or count_user > n:
            count_user = int(input(f"Вы ошиблись, попробуйте заново\nСколько Вы хотите взять конфет?(от 1 до {n}): "))
    
    n = n - count_user
    print(f'Вы взяли: {count_user}\nОсталось {n} конфет')
    result = check_win(j, n)
    if result:
        print(result)
        exit()
    j = 1
    if n < 28:
        count_bot = rd(1, n)
    else:
        count_bot = rd(1, 28)
    n = n - count_bot
    print(f'Бот взял: {count_bot}\nОсталось {n} конфет')
    result = check_win(j, n)
    j = 0
    if result:
        print(result)
        exit()

# b) Подумайте как наделить бота ""интеллектом""

