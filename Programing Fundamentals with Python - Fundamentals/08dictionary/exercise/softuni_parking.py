number_of_commands = int(input())
registered = {}
unregistered = []
for parking in range(number_of_commands):
    command = input().split(" ")
    if command[0] == 'register':
        name = command[1]
        number = command[2]

        if name not in registered.keys():
            registered[name] = number
            print(f"{name} registered {registered[name]} successfully")
        else:
            print(f"ERROR: already registered with plate number {number}")
    elif command[0] == 'unregister':
        name = command[1]

        if name not in registered.keys():
            print(f"ERROR: user {name} not found")
        else:
            unregistered.append(name)
            registered.pop(name)
            print(f"{name} unregistered successfully")
for username, license_plate in registered.items():
    print(f"{username} => {license_plate}")
