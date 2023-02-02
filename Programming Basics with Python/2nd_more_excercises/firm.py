project_hours = int(input())
days = int(input())
workers = int(input())
from math import floor

total_days = days * 0.90

project = total_days * 8
work_done = workers * (days * 2)
total_hours = project + work_done
difference = floor(total_hours - project_hours)
if total_hours >= project_hours:
    print(f'Yes!{difference} hours left.')
else:
    print(f'Not enough time!{abs(difference)} hours needed.')


