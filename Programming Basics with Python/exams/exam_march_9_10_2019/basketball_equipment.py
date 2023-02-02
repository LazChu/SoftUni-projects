annual_tax = int(input())

sneakers = annual_tax * 0.60
basketball_outfit = sneakers * 0.80
ball = basketball_outfit / 4
accessories = ball / 5

total_price = annual_tax + sneakers + basketball_outfit + ball + accessories
print(f'{total_price:.2f}')