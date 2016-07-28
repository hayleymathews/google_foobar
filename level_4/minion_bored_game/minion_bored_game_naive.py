from itertools import product
from pprint import pprint

def answer(t, n):
    if n == 1:
        return 1
    sides = ['Left', 'Right', 'Stay']
    games = list(product(sides, repeat=t))
    total_games = len(games)
    winning_games = 0
    losing_games = 0
    for game in list(games):
        position = 1
        for index, play in enumerate(game):
            if play == 'Left':
                position += 1
            elif play == 'Right':
                position -= 1
            if position < 1:
                games.remove(game)
                break
            elif index + 1 != t and position == n and game[index + 1] != 'Stay':
                games.remove(game)
                break
            if position != n:
                if game in games:
                    games.remove(game)
    winning_games = len(games)
    losing_games = total_games - winning_games
    return(winning_games)
