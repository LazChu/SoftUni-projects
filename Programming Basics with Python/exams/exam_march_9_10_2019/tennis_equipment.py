import math

tennis_racket = float(input())
number_tennis_rackets = int(input())
number_sneakers_pairs = int(input())

price_tennis_rackets = tennis_racket * number_tennis_rackets
price_sneakers_pair = tennis_racket / 6
price_sneakers = price_sneakers_pair * number_sneakers_pairs
extra_equipment = (price_tennis_rackets + price_sneakers) * 0.20
total_price = price_tennis_rackets + price_sneakers + extra_equipment
amount_tennis_player = total_price / 8
amount_sponsor = total_price * 7 / 8

print(f"Price to be paid by Djokovic {math.floor(amount_tennis_player)}")
print(f"Price to be paid by sponsors {math.ceil(amount_sponsor)}")