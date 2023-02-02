team_name = input()
games_played = int(input())

points = 0
win = 0
draw = 0
loss = 0

if games_played <= 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    for games in range(games_played):
        result = input()
        if result == "W":
            points += 3
            win += 1
        elif result == 'D':
            points += 1
            draw += 1
        else:
            points += 0
            loss += 1
    percent_wins = win / games_played * 100
    print(f"{team_name} has won {points} points during this season.")
    print('Total stats:')
    print(f"## W: {win}")
    print(f"## D: {draw}")
    print(f"## L: {loss}")
    print(f"Win rate: {percent_wins:.2f}%")