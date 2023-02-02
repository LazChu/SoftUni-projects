products = input().split(' ')
searched_products = input().split(' ')
bakery = {}
for product in range(0, len(products), 2):
    key = products[product]
    value = products[product + 1]
    bakery[key] = int(value)
for product in searched_products:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
