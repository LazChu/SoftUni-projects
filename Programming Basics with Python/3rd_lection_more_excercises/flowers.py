chrysanthemums_number = int(input())
roses_number = int(input())
tulips_number = int(input())
season = input()
type_of_day = input()


if season == 'Spring' or season == 'Summer':
    chrysanthemums_price = chrysanthemums_number * 2
    roses_price = roses_number * 4.10
    tulips_price = tulips_number * 2.50
else:
    chrysanthemums_price = chrysanthemums_number * 3.75
    roses_price = roses_number * 4.50
    tulips_price = tulips_number * 4.15

total_flowers = chrysanthemums_number + roses_number + tulips_number
flowers_price = chrysanthemums_price + roses_price + tulips_price

if type_of_day == 'Y':
    flowers_price = flowers_price + (flowers_price * 0.15)
else:
    flowers_price = flowers_price

if tulips_price > 7 and season == 'Spring':
    flowers_price *= 0.95
elif roses_number >= 10 and season == 'Winter':
    flowers_price *= 0.90
if total_flowers > 20:
    flowers_price *= 0.80
else:
    flowers_price = flowers_price
total_price = flowers_price + 2
print(f'{total_price:.2f}')
