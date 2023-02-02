lenght_meters = float(input())
width_meters = float(input())
lenght_in_cm = lenght_meters*100
widht_in_cm = width_meters*100
coridor=100
workspace_widht = 70
work_space_lenght = 120
top_side = widht_in_cm-coridor
top_side_workbenches = top_side//workspace_widht
bottom_side_workbenches = lenght_in_cm//work_space_lenght
total_benches= top_side_workbenches*bottom_side_workbenches-3
print(int(total_benches))