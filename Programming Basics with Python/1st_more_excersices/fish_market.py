mackerel_price = float(input())
anchovies_price = float(input())
bonito_kg = float(input())
scad_kg = float(input())
clams_kg = int(input())
bonito = mackerel_price + (mackerel_price*0.60)
bonito_price = bonito_kg * bonito
scad = anchovies_price + (anchovies_price*0.80)
scad_price = scad_kg * scad
clams = clams_kg * 7.5
total=bonito_price + scad_price + clams
print(f'{total:.2f}')