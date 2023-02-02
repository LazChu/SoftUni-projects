eggs_in_stock = int(input())

command = input()
total_eggs = eggs_in_stock
sold_eggs = 0
while command != 'Close':

    if command == 'Buy':
        eggs = int(input())
        if eggs > total_eggs:
            # diff = eggs - total_eggs
            print("Not enough eggs in store!")
            print(f"You can buy only {total_eggs}.")
            break
        total_eggs -= eggs
        sold_eggs += eggs
    elif command == 'Fill':
        eggs = int(input())
        total_eggs += eggs
    command = input()
if command == 'Close':
    print('Store is closed!')
    print(f"{sold_eggs} eggs sold.")
