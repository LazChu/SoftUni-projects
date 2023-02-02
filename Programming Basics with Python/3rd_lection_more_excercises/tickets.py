budget = float(input())
category_ticket = input()
people = int(input())

ticket_price = 0
transport = 0
if category_ticket == 'VIP':
    ticket_price = 499.99
else:
    ticket_price = 249.99

if 1 <= people <= 4:
    transport = budget * 0.75
elif people < 10:
    transport = budget * 0.60
elif people < 25:
    transport = budget * 0.50
elif people < 50:
    transport = budget * 0.40
else:
    transport = budget * 0.25

tickets = ticket_price * people
cost = tickets + transport
diff = abs(budget - cost)
if budget >= cost:
    print(f"Yes! You have {diff:.2f} leva left.")
elif budget < cost:
    print(f"Not enough money! You need {diff:.2f} leva.")