import random
import os
def clear(): return os.system('cls')


clear()


def game_vs_AI():
    player1 = input("Введите имя первого игрока: ")
    player2 = ("Artificial Intelligence")
    value = int(input("Введите количество конфет на столе: "))
    value_max = int(input("Введите максимальное количество конфет за ход: "))
    turn = random.choice([player1, player2])
    while value > 0:
        print(f"{turn} твой ход")
        if turn == player2:
            if value == value_max:
                count = value
            elif value % value_max == 0:
                count = value_max-1
            else:
                count = value % value_max-1
                if count == 0:
                    count =1
            print(count)
        else:
            count = int(input("Сколько конфет возьмее? "))
        if count > value_max or count > value:
            print(f'Это слишком много, можно взять не более {value_max} конфет, у нас всего {value} конфет')
        else:
            value -= count
            if value > 0:
                print(f"Конфет осталось --> {value}")
            else:
                print(f"Конфет не осталось!(")

            turn = player2 if turn == player1 else player1

    winner = player2 if turn == player1 else player1
    print(f'Победитель --> {winner}')


game_vs_AI()
