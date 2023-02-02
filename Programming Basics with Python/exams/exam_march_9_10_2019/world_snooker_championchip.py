tournament_stage = input()
ticket_type = input()
number_of_tickets = int(input())
picture_with_the_trophy = input()

picture = 40

if tournament_stage == 'Quarter final':
    if ticket_type == 'Standard':
        price = 55.50
    elif ticket_type == 'Premium':
        price = 105.20
    elif ticket_type == 'VIP':
        price = 118.90
elif tournament_stage == 'Semi final':
    if ticket_type == 'Standard':
        price = 75.88
    elif ticket_type == 'Premium':
        price = 125.22
    elif ticket_type == 'VIP':
        price = 300.40
elif tournament_stage == 'Final':
    if ticket_type == 'Standard':
        price = 110.10
    elif ticket_type == 'Premium':
        price = 160.66
    elif ticket_type == 'VIP':
        price = 400

tickets_cost = number_of_tickets * price
if tickets_cost > 4000:
    tickets_cost = tickets_cost - (tickets_cost * 0.25)
    if picture_with_the_trophy == 'Y':
        picture = 0
elif tickets_cost > 2500:
    tickets_cost = tickets_cost - (tickets_cost * 0.10)
if picture_with_the_trophy == 'Y':
    tickets_cost = tickets_cost + (picture * number_of_tickets)
print(f'{tickets_cost:.2f}')
