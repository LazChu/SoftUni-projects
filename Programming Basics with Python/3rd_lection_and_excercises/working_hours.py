hour = int(input())
day = input()

working_days = day =='Monday' or day == 'Tuesday' or day == 'Wednesday' or\
    day == 'Thursday' or day == 'Friday' or day == 'Saturday'
if working_days and 10 <= hour <= 18:
    print('open')
if day == 'Sunday' or hour < 10 or hour > 18:
    print('closed')