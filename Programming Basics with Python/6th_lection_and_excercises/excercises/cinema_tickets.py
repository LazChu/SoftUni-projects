command = input()


student_tickets = 0
standard_tickets = 0
kids_tickets = 0
total_tickets_sold = 0
while command != 'Finish':
    movie_name = command
    free_seats = int(input())
    total_seats = free_seats
    sold_tickets = 0
    while free_seats > 0:
        ticket_type = input()
        if ticket_type == 'End':
            break
        elif ticket_type == 'student':
            student_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
        else:
            kids_tickets += 1
        free_seats -= 1
        sold_tickets += 1
    percent_full_hall = sold_tickets / total_seats * 100
    print(f'{movie_name} - {percent_full_hall:.2f}% full.')
    total_tickets_sold = student_tickets + kids_tickets + standard_tickets
    command = input()
percent_student_tickets = student_tickets / total_tickets_sold * 100
percent_standard_tickets = standard_tickets / total_tickets_sold * 100
percent_kids_tickets = kids_tickets / total_tickets_sold * 100

print(f"Total tickets: {total_tickets_sold}")
print(f'{percent_student_tickets:.2f}% student tickets.')
print(f"{percent_standard_tickets:.2f}% standard tickets.")
print(f"{percent_kids_tickets:.2f}% kids tickets.")




