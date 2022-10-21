from random import randint, choice

hello = ('Привет, давай играть? На столе лежит 150 конфет. Играют два игрока делая ход друг после друга.'
            'За один ход можно забрать не более чем 28 конфет.'
            'Все конфеты оппонента достаются сделавшему последний ход')
print(hello)  

def name_players():
    player1 = input('Как Вас зовут?\n')
    player2 = 'Гена'
    print(f'Очень приятно, меня зовут {player2}')
    return [player1, player2]


def get_rules(players):
    n = int(150)
    m = int(28)
    first = int(input(f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
    if first != 1:
        first = 0
    return [n, m, int(first)]


messages = ['Берите конфеты', 'Возьмите конфеты', 
            'Ваш ход', 'Сколько дать конфет?', 'Ход за Вами']


def play_game(rules, players, messages):
    count = rules[2]
    if rules[0] % 10 == 1 and 9 > rules[0] > 10:
        letter = 'а'
    elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
        letter = 'ы'
    else:
        letter = ''
    while rules[0] > 0:
        if not count % 2:
            move = randint(1, rules[1])
            print(f'Я забираю {move}')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(
                    f'Слишком много, можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}')
                attempt = 3
                while attempt > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'У Вас не осталось попыток. Вы проиграли!')
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f'Осталось {rules[0]} конфет{letter}')
        else:
            print('Конфет не осталось.')
        count += 1
    return players[count % 2]

players = name_players()
rules = get_rules(players)
 
winer = play_game(rules, players, messages)
if not winer:
    print('У нас нет победителя.')
else: print(f'Поздравляю! Победил {winer}! Ему достаются все конфеты!')