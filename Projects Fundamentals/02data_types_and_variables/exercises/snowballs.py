number_snowballs = int(input())

best_weight = 0
best_time = 0
best_quality = 0
best_value = 0

for snowball in range(number_snowballs):
    snowball_weight = int(input())
    time_needed = int(input())
    quality_snowball = int(input())
    value = (snowball_weight / time_needed) ** quality_snowball
    if value > best_value:
        best_weight = snowball_weight
        best_time = time_needed
        best_quality = quality_snowball
        best_value = value
print(f"{best_weight} : {best_time} = {int(best_value)} ({best_quality})")

