annual_tax = int(input())
sneakers = annual_tax - (annual_tax * 0.40)
clothes = sneakers - (sneakers * 0.20)
ball = clothes * 0.25
accessories = ball * 0.20
total_price = annual_tax + sneakers + clothes + ball + accessories
print(total_price)
