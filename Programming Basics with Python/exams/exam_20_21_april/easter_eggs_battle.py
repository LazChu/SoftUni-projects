first_player = int(input())
second_player = int(input())

command = input()
eggs_one = first_player
eggs_two = second_player
while command != 'End of battle':
    winner = command
    if winner == 'one':
        eggs_two -= 1
        if eggs_two <= 0:
            print(f"Player two is out of eggs. Player one has {eggs_one} eggs left.")
            break
    elif winner == 'two':
        eggs_one -= 1
        if eggs_one <= 0:
            print(f"Player one is out of eggs. Player two has {eggs_two} eggs left.")
            break
    command = input()
if command == 'End of battle':
    print(f"Player one has {eggs_one} eggs left.")
    print(f"Player two has {eggs_two} eggs left.")