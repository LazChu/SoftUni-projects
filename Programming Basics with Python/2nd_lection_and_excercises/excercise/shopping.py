budget = float(input())
graphics_card = int(input())
cpu = int(input())
ram = int(input())
gc_price = graphics_card * 250
cpu_price = gc_price * 0.35 * cpu
ram_price = gc_price * 0.10 * ram
price = gc_price + cpu_price + ram_price
if graphics_card > cpu:
    price = price -( price * 0.15)
difference = abs(budget - price)
if budget >= price:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")