tour = input()
lenght = len(tour)
command = input()
while command != 'Travel':
    action = command.split(":")
    if action[0] == "Add Stop":
        index = int(action[1])
        new_stop = action[2]
        if 0 <= index < len(tour):
            tour = tour[:index] + new_stop + tour[index:]
    elif action[0] == "Remove Stop":
        start = int(action[1])
        end = int(action[2])
        if 0 <= start < len(tour) and 0 <= end < len(tour):
            tour = tour[:start] + tour[end + 1:]
    elif action[0] == "Switch":
        old_string = action[1]
        new_string = action[2]
        if old_string in tour:
            tour = tour.replace(old_string, new_string)
    print(tour)
    command = input()
print(f"Ready for world tour! Planned stops: {tour}")
