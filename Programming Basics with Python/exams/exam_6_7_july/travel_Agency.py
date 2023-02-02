town = input()
booking_type = input()
vip_discount = input()
days = int(input())

if days >= 7:
    days -= 1
elif days <= 1:
    print("Days must be positive number!")

if town == 'Bansko' or town == 'Borovets':
    if booking_type == "withEquipment":
        price = 100
        if vip_discount == 'yes':
            price *= 0.90
    elif booking_type == 'noEquipment':
        price = 80
        if vip_discount == 'yes':
            price *= 0.95
    else:
        print('Invalid input!')
    total_price = days * price
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
elif town == 'Varna' or town == 'Burgas':
    if booking_type == "withBreakfast":
        price = 130
        if vip_discount == 'yes':
            price *= 0.88
    elif booking_type == "noBreakfast":
        price = 100
        if vip_discount == 'yes':
            price *= 0.93
    total_price = days * price
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
else:
    print('Invalid input!')
