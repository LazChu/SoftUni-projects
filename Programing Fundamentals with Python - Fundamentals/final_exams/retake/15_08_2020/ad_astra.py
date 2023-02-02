import re

food_input = input()
pattern = r"(\#|\|)([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1"
result = re.findall(pattern, food_input)

total_calories = 0

for match in result:
    food_type = match[1]
    expiry_date = match[2]
    calories = int(match[3])
    total_calories += calories
days = total_calories // 2000

print(f"You have food to last you for: {days} days!")
for match in result:
    print(f"Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[3]}")
