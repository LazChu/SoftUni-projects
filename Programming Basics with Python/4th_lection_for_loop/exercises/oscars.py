actor_name = input()
academy_points = float(input())
jury = int(input())

for points in range(jury):
    current_name = input()
    current_points = float(input())
    current_final_points = len(current_name) * current_points / 2
    academy_points += current_final_points
    if academy_points > 1250.5:
        break
if academy_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
else:
    diff = 1250.5 - academy_points
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")