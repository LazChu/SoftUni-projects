import re

string = input()

pattern = r"(\=|\/)([A-Z]{1}[A-Za-z]{2,})\1"
result = re.findall(pattern,string)

destination = []
travel_points = 0
for town in result:
    destination.append(town[1])
    travel_points += len(town[1])
print(f"Destinations: {', '.join(destination)}")
print(f"Travel Points: {travel_points}")