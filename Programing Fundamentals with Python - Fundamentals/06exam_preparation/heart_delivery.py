neigbourghood = list(map(int, input().split('@')))
command = input()
jump_distance = 0
valentines = 0
failed_places = 0
while command != 'Love!':
    jump = command.split()
    length = int(jump[1])
    jump_distance += length
    # neigbourghood[jump_distance] -= 2
    if len(neigbourghood) < jump_distance:
        jump_distance = 0
    neigbourghood[jump_distance] -= 2
    if 0 in neigbourghood:
        print(f"Place {neigbourghood.index(0)} has Valentine's day.")
        for house in neigbourghood:
            if house != 0:
                failed_places += 1

    command = input()
print(f"Cupid's last position was {jump_distance}.")
print(f"Cupid has failed {failed_places} places.")
