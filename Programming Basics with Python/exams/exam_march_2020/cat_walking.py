minutes_walk_per_day = int(input())
walks_per_day = int(input())
calories_intake = int(input())

total_walking_time = minutes_walk_per_day * walks_per_day
calories_burned = total_walking_time * 5
calories_needed = calories_intake / 2

if calories_burned >= calories_needed:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.")