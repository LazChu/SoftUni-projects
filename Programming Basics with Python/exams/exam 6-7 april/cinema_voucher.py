voucher = int(input())
command = input()

while command != 'End':
    purchase = command
    purchase_len = len(purchase)
    for index,letter in enumerate(purchase):
        if purchase_len > 8:
            # ticket_price = letter[0]+ letter[1]
            ticket_price = chr(int(letter[0])) + chr(int(letter[1]))
            print(ticket_price)