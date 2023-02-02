# figures: square,rectangle,circle,triangle
figure = input()

if figure == 'square':
    side_a =float(input())
    face_square = side_a*side_a
    print(f'{face_square:.3f}')
elif figure == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    face_rectangle = side_a*side_b
    print(f'{face_rectangle:.3f}')
elif figure == 'circle':
    import math
    radius_circle = float(input())
    radius = math.pi*(radius_circle*radius_circle)
    print(f'{radius:.3f}')
elif figure == 'triangle':
    side_a = float(input())
    height = float(input())
    face_triangle = (side_a*height)/2
    print(f'{face_triangle:.3f}')