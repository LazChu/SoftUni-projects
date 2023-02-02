number_pages = int(input())
pages_per_hour = int(input())
days_needed = int(input())
total_time_needed = number_pages/pages_per_hour
hours_per_day = total_time_needed/days_needed
print(int(hours_per_day))