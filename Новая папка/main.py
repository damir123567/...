from random import randint
from time import sleep
from heplers import *
from data import *

name = input('Введи своё имя, путник: ')
player['name'] = name
current_enemy = 0

while True:
    action = input('''Выбери действие:
1 - В бой!
2 - Тренировка
''')
    if action == '1':
        current_enemy = fight(current_enemy)
        if current_enemy == 3:
            break
    elif action == '2':
        training_type = input('''1 - тренировать атаку
2 - тренировать оборону
''')
        training(training_type)

        
            


