player_one = input()
player_two = input()
command = input()

total_points_player_one = 0
total_points_player_two = 0
points = 0
number_wars = False

while command != 'End of game':
    card_one = int(command)
    card_two = int(input())
    if card_one > card_two:
        player_one_points = card_one - card_two
        total_points_player_one += player_one_points
    elif card_two > card_one:
        player_two_points = card_two - card_one
        total_points_player_two += player_two_points
    elif card_one == card_two:
        number_wars = True
        extra_card_one = int(input())
        extra_card_two = int(input())
        if extra_card_one > extra_card_two:
            points = total_points_player_one
            winner = player_one
            break
        else:
            points = total_points_player_two
            winner = player_two
            break
    command = input()
if number_wars:
    print('Number wars!')
    print(f"{winner} is winner with {points} points")
else:
    print(f"{player_one} has {total_points_player_one} points")
    print(f"{player_two} has {total_points_player_two} points")
