command = input()
total_price = 0
total_price_with_tax = 0
taxes = 0
while True:
    if command == 'special' or command == 'regular':
        break
    price = float(command)
    if price < 0:
        print("Invalid price!")
        command = input()
        continue
    total_price += price
    command = input()

taxes = total_price * 0.20
total_price_with_tax = taxes + total_price
if total_price_with_tax == 0:
    print('Invalid order!')
elif command == 'special':
    total_price_with_tax -= total_price_with_tax * 0.10
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total_price:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    print(f'Total price: {total_price_with_tax:.2f}$')
else:
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total_price:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    print(f'Total price: {total_price_with_tax:.2f}$')
