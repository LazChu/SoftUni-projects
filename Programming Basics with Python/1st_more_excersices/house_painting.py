wall_height = float(input())
wall_lenght = float(input())
roof_height = float(input())

side_wall = wall_height * wall_lenght
window = (1.5 * 1.5) * 2
door = 1.2 * 2
back_wall = wall_height * wall_height
walls = side_wall * 2 + back_wall * 2
wall_area = walls - window - door
paint_walls = wall_area / 3.4

side_roof = (wall_lenght * wall_height) * 2
front_part = (roof_height * wall_height) * 2 / 2
roof_area = side_roof + front_part
paint_roof = roof_area / 4.3
print(f'{paint_walls:.2f}')
print(f'{paint_roof:.2f}')