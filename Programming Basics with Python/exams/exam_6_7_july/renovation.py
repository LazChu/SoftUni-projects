import math

height = int(input())
width = int(input())
paint_free_percent = int(input())

total_paint = 0

input_line = input()
while input_line != "Tired!":
    liters_paint = int(input_line)
    walls = height * width * 4
    paint_free = walls * paint_free_percent / 100
    area = walls - paint_free
    total_paint += liters_paint
    painted_area = area - total_paint
    if painted_area < 0:
        liters = abs(total_paint - area)
        print(f"All walls are painted and you have {int(liters)} l paint left!")
        break
    elif painted_area == 0:
        print("All walls are painted! Great job, Pesho!")
        break
    input_line = input()
if input_line == 'Tired!':
    print(f"{math.ceil(painted_area)} quadratic m left.")