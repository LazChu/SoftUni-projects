player_one_eggs = int(input())
player_two_eggs = int(input())
command = input()
eggs_one = player_one_eggs
eggs_two = player_two_eggs

while command != "End of battle":
    player = command
    if player == 'one':
        eggs_two -= 1
    elif player == 'two':
        eggs_one -= 1
    if eggs_one <= 0:
        print(f"Player one is out of eggs. Player two has {eggs_two} eggs left.")
        break
    elif eggs_two <= 0:
        print(f"Player two is out of eggs. Player one has {eggs_one} eggs left.")
        break
    command = input()
if command == 'End of battle':
    print(f"Player one has {eggs_one} eggs left.")
    print(f"Player two has {eggs_two} eggs left.")