# Игра с кончетами. Дано N конфет.
# Каждый игрок за каждый ход может взять не более M конфет.
# Побеждает игрок,забравший последнюю конфету.

# man vs man
import os
clear = lambda: os.system('cls')
clear()
import random


def game():
    player1 = input("Введите имя первого игрока: ")
    player2 = input("Введите имя второго игрока: ")
    value = int(input("Введите количество конфет на столе: "))
    value_max = int(input("Введите максимальное количество конфет за ход: "))
    turn = random.choice([player1,player2])
    while value>0:
        print(f"{turn} твой ход")
        count = int(input("Сколько конфет возьмее? "))
        if count > value_max or count >value:
            print(f'Это слишком много, можно взять не более {value_max} конфет, у нас всего {value} конфет')
        else:
            value-=count
            if value>0:
                print(f"Конфет осталось --> {value}")
            else:
                print(f"Конфет не осталось!(")

            turn = player2 if turn == player1 else player1
    
    winner = player2 if turn == player1 else player1
    print(f'Победитель --> {winner}')

game()