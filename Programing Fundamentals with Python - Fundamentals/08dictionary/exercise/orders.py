command = input()

products = {}

while command != "buy":
    info = command.split(" ")
    name = info[0]
    price = float(info[1])
    quantity = int(info[2])
    total_quantity = quantity
    if name not in products:
        products[name] = {}
        products[name][price] = quantity

    else:
        udpated_quantity = quantity + products[name][price]

    command = input()
