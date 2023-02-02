company_name = input()
adult_tickets = int(input())
child_tickets = int(input())
price_adult_ticket = float(input())
service_tax = float(input())

price_child_tickets = price_adult_ticket * 0.30

adult_price = (price_adult_ticket + service_tax) * adult_tickets
kids_price = (price_child_tickets + service_tax) * child_tickets

profit = (adult_price + kids_price) * 0.20

print(f"The profit of your agency from {company_name} tickets is {profit:.2f} lv.")