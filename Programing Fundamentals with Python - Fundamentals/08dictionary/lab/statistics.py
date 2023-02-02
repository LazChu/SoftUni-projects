command = input()
procuts_dict = {}
while command != 'statistics':
    products = command.split(': ')
    key = products[0]
    value = int(products[1])
    if key not in procuts_dict:
        procuts_dict[key] = 0
    procuts_dict[key] += value
    command = input()
print("Products in stock:")
for product,quantity in procuts_dict.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(procuts_dict.keys())}")
print(f"Total Quantity: {sum(procuts_dict.values())}")