world_record = float(input())
distance = float(input())
time_per_meter = float(input())

resistance = distance // 15 * 12.5
new_record = distance * time_per_meter + resistance


difference = abs(world_record - new_record)
if new_record < world_record:
    print(f" Yes, he succeeded! The new world record is {new_record:.2f} seconds.")
else:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")