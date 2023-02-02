import math

number_of_tournaments = int(input())
starting_points = int(input())
won = 0
points = 0
total_points = 0
for tournaments in range(number_of_tournaments):
    stage = (input())
    if stage == 'W':
        points += 2000
        won += 1
    elif stage == 'F':
        points += 1200
    elif stage == 'SF':
        points += 720
    total_points = starting_points + points
average_points = math.floor(points/ number_of_tournaments)
tournament_won = won / number_of_tournaments * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f'{tournament_won:.2f}%')