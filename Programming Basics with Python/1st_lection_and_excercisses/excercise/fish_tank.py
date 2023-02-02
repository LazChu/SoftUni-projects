lenght_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent = float(input())
fish_tank_face = lenght_cm*width_cm*height_cm
volume_litres=fish_tank_face*0.001
total_capacity = volume_litres-((volume_litres*percent)/100)
print(total_capacity)