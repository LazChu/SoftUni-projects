hour_exam = int(input())
minutes_exam = int(input())
hour_arriving = int(input())
minutes_arriving = int(input())


time_of_exam = hour_exam * 60 + minutes_exam
arriving_time = hour_arriving * 60 + minutes_arriving

if arriving_time > time_of_exam:
    print('Late')
elif time_of_exam - 30 <= arriving_time <= time_of_exam:
    print('On time')
else:
    print('Early')

difference = abs(arriving_time - time_of_exam)
hours = difference // 60
minutes = difference % 60
if time_of_exam - 60 < arriving_time < time_of_exam:
    print(f"{difference} minutes before the start")
elif arriving_time <= time_of_exam - 60:
    print(f"{hours}:{minutes:02d} hours before the start")
elif time_of_exam < arriving_time < time_of_exam + 60:
    print(f"{difference} minutes after the start")
elif arriving_time >= time_of_exam + 60:
    print(f"{hours}:{minutes:02d} hours after the start")