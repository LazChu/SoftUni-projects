load_capacity = float(input())
input_line = input()
case_counter = 0
extra_volume = 0
total_case_volume = 0
no_more_free_space = False
while input_line != 'End':
    case_volume = float(input_line)
    total_case_volume += case_volume + extra_volume
    if total_case_volume >= load_capacity:
        no_more_free_space = True
        break
    case_counter += 1
    if case_counter % 3 == 0:
        volume = case_volume * 0.10
        extra_volume += volume
        case_counter -= 1

    input_line = input()
if no_more_free_space:
    print("No more space!")
if input_line == 'End':
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {case_counter} suitcases loaded.")



# ======================================



load_capacity = float(input())
input_line = input()
case_counter = 0
total_case_volume = 0

while input_line != 'End':
    case_volume = float(input_line)
    case_counter += 1

    if case_counter % 3 == 0:
        case_volume *= 1.1

    total_case_volume += case_volume
    if total_case_volume > load_capacity:
        case_counter -= 1
        break
    input_line = input()
if total_case_volume > load_capacity:
    print("No more space!")
else:
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {case_counter} suitcases loaded.")


