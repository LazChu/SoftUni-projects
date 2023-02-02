lines = int(input())
water_poored_in = 0
capacity = 255
for litres in range(lines):
    water = int(input())
    water_poored_in += water
    if water_poored_in > capacity:
        print('Insufficient capacity!')
        water_poored_in -= water
print(water_poored_in)