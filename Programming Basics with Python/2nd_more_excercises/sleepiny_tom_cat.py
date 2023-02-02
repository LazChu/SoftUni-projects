number_day_offs = int(input())

# 	•	Когато е на работа, стопанинът му си играе с него по 63 минути на ден.
# 	•	Когато почива, стопанинът му си играе с него  по 127 минути на ден.
norm_play_time = 30000
work_days = 365 - number_day_offs
play_time_in_minutes = work_days * 63 + number_day_offs * 127
difference = abs(norm_play_time - play_time_in_minutes)
hours = difference // 60
minutes = difference % 60

if play_time_in_minutes >= norm_play_time:
    print('Tom will run away')
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')