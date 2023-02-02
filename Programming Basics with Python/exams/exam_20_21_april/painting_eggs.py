eggs_size = input()
egg_color = input()
number_eggs = int(input())

if egg_color == 'Red':
    if eggs_size == 'Large':
        price = number_eggs * 16
    elif eggs_size == 'Medium':
        price = number_eggs * 13
    elif eggs_size == 'Small':
        price = number_eggs * 9
elif egg_color == 'Green':
    if eggs_size == 'Large':
        price = number_eggs * 12
    elif eggs_size == 'Medium':
        price = number_eggs * 9
    elif eggs_size == 'Small':
        price = number_eggs * 8
elif egg_color == 'Yellow':
    if eggs_size == 'Large':
        price = number_eggs * 9
    elif eggs_size == 'Medium':
        price = number_eggs * 7
    elif eggs_size == 'Small':
        price = number_eggs * 5
total_price = price - (price * 0.35)
print(f"{total_price:.2f} leva.")