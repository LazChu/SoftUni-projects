cake_width = int(input())
cake_length = int(input())
cake_pieces = cake_length * cake_width
cake_is_over = False
command = input()
while command != 'STOP':
    current_pieces_cake = int(command)
    cake_pieces -= current_pieces_cake
    if cake_pieces < 0:
        cake_is_over = True
        break
    command = input()
if cake_is_over:
    print(f"No more cake left! You need {abs(cake_pieces)} pieces more.")
else:
    print(f"{cake_pieces} pieces are left.")