# def shootin_targets(targets):


targets = list(map(int, input().split()))

command = input()
while command != 'End':
    shot = command
    # targets[int(shot)] -= 1
    if int(command) >= len(targets):
        command = input()
        continue
    targets[:] = [number - targets[int(shot)] for number in targets]


    targets[int(shot)] -= 1
    command = input()
