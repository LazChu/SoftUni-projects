number = int(input())
all_pieces = {}
for number_of_pieces in range(number):
    given_piece = input().split("|")
    piece = given_piece[0]
    composer = given_piece[1]
    key = given_piece[2]
    all_pieces[piece] = {}
    all_pieces[piece][composer] = key
command = input()
while command != "Stop":
    current_command = command.split("|")
    action = current_command[0]
    piece = current_command[1]
    if action == "Add":
        composer = current_command[2]
        key = current_command[3]
        if piece not in all_pieces.keys():
            all_pieces[piece] = {}
            all_pieces[piece][composer] = key
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif action == "Remove":
        if piece in all_pieces.keys():
            print(f"Successfully removed {piece}!")
            all_pieces.pop(piece)
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif action == "ChangeKey":
        new_key = current_command[2]
        if piece in all_pieces.keys():
            pass
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()
print()