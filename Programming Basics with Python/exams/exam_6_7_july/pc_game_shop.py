sold_games = int(input())
game_sold = 0
game_one = 0
game_two = 0
game_three = 0
other_games = 0
for games in range(sold_games):
    game = input()
    game_sold += 1
    if game == 'Hearthstone':
        game_one += 1
    elif game == 'Fornite':
        game_two += 1
    elif game == 'Overwatch':
        game_three += 1
    else:
        other_games += 1
percent_game_one = game_one / game_sold * 100
percent_game_two = game_two / game_sold * 100
percent_game_three = game_three / game_sold * 100
percent_other_games = other_games / game_sold * 100

print(f"Hearthstone - {percent_game_one:.2f}%")
print(f"Fornite - {percent_game_two:.2f}%")
print(f"Overwatch - {percent_game_three:.2f}%")
print(f"Others - {percent_other_games:.2f}%")