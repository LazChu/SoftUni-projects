square_meters = float(input())
square_meter_price = 7.61
price = square_meters * square_meter_price
discount = price * 0.18
total_price = price - discount
print(f'The final price is: {total_price} lv.')
print(f'The discount is: {discount} lv.')
