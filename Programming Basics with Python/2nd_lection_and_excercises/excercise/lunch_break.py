import math
name = input()
episode_lenght = int(input())
lunch_break = int(input())

lunch = lunch_break / 8
rest = lunch_break / 4
time_left = lunch_break - lunch - rest
extra_time = abs(time_left - episode_lenght)
if time_left > episode_lenght:
    print(f"You have enough time to watch {name} and left with {math.ceil(extra_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {math.ceil(extra_time)} more minutes.")