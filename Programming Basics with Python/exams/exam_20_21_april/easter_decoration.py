basket = 1.50
wreath = 3.80
chocolate_bunny = 7

clients = int(input())
total_price = 0
bought_items = 0
money_spend = 0
avg_price = 0
for customers in range(clients):
    command = input()
    total_price = 0
    bought_items = 0
    while command != 'Finish':
        bought_items += 1
        if command == 'basket':
            price = 1.50
        elif command == 'wreath':
            price = 3.80
        elif command == 'chocolate bunny':
            price = 7
        command = input()
        total_price += price
    if bought_items % 2 == 0:
        total_price = total_price - (total_price * 0.20)
        print(f"You purchased {bought_items} items for {total_price:.2f} leva.")
    else:
        print(f"You purchased {bought_items} items for {total_price:.2f} leva.")
    money_spend += total_price
avg_price = money_spend / clients
print(f"Average bill per client is: {avg_price} leva.")