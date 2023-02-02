pirate_ship_status = list(map(int, input().split('>')))
warship_status = list(map(int, input().split('>')))
section_maximum_health = int(input())
command = input()
sections = 0
ship_not_sinced = False
while command != 'Retire':
    current_action = command.split()
    action = current_action[0]
    if action == 'Fire':
        index = current_action[1]
        demage = current_action[2]
        if int(index) < len(warship_status):
            warship_status[int(index)] -= int(demage)
            if [value for value in warship_status if value <= 0]:
                print("You won! The enemy ship has sunken.")
                exit()
    elif action == 'Defend':
        start_index = int(current_action[1])
        end_index = int(current_action[2])
        demage = int(current_action[3])
        if start_index >= 0:
            if len(pirate_ship_status) > end_index:
                for section in range(start_index, end_index + 1):
                    pirate_ship_status[section] -= demage
                    if pirate_ship_status[section] > section_maximum_health:
                        pirate_ship_status[section] = section_maximum_health
                    if [value for value in pirate_ship_status if value <= 0]:
                        print("You lost! The pirate ship has sunken.")
                        exit()
    elif action == 'Repair':
        index = current_action[1]
        health = current_action[2]
        pirate_ship_status[int(index)] += int(health)
    elif action == 'Status':
        for section in pirate_ship_status:
            current_section_health = section_maximum_health * 0.20
            if section < current_section_health:
                sections += 1
        print(f"{sections} sections need repair.")
    command = input()
else:
    pirate_ship_sum = sum(pirate_ship_status)
    warship_sum = sum(warship_status)
    print(f"Pirate ship status: {pirate_ship_sum}")
    print(f"Warship status: {warship_sum}")
