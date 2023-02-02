target = 10000
total_steps = 0

while total_steps < target:
    command = input()
    if command == 'Going home':
        steps_to_home = int(input())
        total_steps += steps_to_home
        break
    current_steps = int(command)
    total_steps += current_steps
diff = abs(total_steps - target)
if total_steps >= target:
    print( "Goal reached! Good job!" )
    print(f"{diff} steps over the goal!")
else:
    print(f'{diff} more steps to reach goal.')