# От лозе с площ X квадратни метри се заделя 40% от реколтата за производство на вино.
# От 1 кв.м лозе се изкарват Y килограма грозде.
# За 1 литър вино са нужни 2,5 кг. грозде.
# Желаното количество вино за продан е Z литра.
# Напишете програма, която пресмята колко вино може да се произведе и дали това количество е достатъчно.
# Ако е достатъчно, остатъкът се разделя по равно между работниците на лозето.
import math
wineyard_square_meters = int(input())
kilos_grape = float(input())
litres_wine_needed = int(input())
number_of_workers = int(input())

grape = (wineyard_square_meters * kilos_grape) * 0.40
litres = grape / 2.5
difference = abs(litres_wine_needed - litres)
wine_left = difference / number_of_workers
if litres < litres_wine_needed:
    print(f"It will be a tough winter! More {math.floor(difference)} liters wine needed.")
elif litres >= litres_wine_needed:
    print(f'Good harvest this year! Total wine: {math.floor(litres)} liters.')
    print(f'{math.ceil(difference)} liters left -> {math.ceil(wine_left)} liters per person.')