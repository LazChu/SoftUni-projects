screening_type = input()
rows = int(input())
colums = int(input())

ticket_price = 0

if screening_type == 'Premiere':
    ticket_price = 12.0
elif screening_type == 'Normal':
    ticket_price = 7.50
elif screening_type == 'Discount':
    ticket_price = 5.00
tickets = ticket_price * rows * colums
print(f'{tickets:.2f}')
