# Магнолии – 3.25
# Зюмбюли – 4
# Рози – 3.50
# Кактуси – 8
# tax = 5%
import math
magnolias = int(input()) * 3.25
hyacinth = int(input()) * 4
roses = int(input()) * 3.50
cactus = int(input()) * 8
present_price = float(input())

order_price = (magnolias + hyacinth + roses + cactus) * 0.95
difference = abs(present_price - order_price)
if order_price >= present_price:
    print(f'She is left with {math.floor(difference)} leva.')
else:
    print(f"She will have to borrow {math.ceil(difference)} leva.")