import math

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds = float(input())

slope_obstacle = 50

time_taken = distance_in_meters * time_in_seconds
slowing_down = math.floor(distance_in_meters / slope_obstacle) * 30
total_time = time_taken + slowing_down
diff = abs(total_time - record_in_seconds)
if total_time < record_in_seconds:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {diff:.2f} seconds slower.")