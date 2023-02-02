command = input()

student_tickets = 0
standard_tickets = 0
kids_tickets = 0
combine_tickets = 0
tickets_sold = 0
cinema_is_full = False

while command != 'Finish':
    movie_name = command
    free_seats = int(input())
    total_seats = free_seats
    for movie in range(free_seats):
        ticket_type = input()
        if total_seats < 0 or ticket_type == 'End':
            cinema_is_full = True
            break
        if ticket_type == 'student':
            student_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
        elif ticket_type == 'kid':
            kids_tickets += 1
        total_seats -= 1
        tickets_sold += 1
        combine_tickets = student_tickets + standard_tickets + kids_tickets
        hall_percentage = tickets_sold / free_seats * 100
    print(f"{movie_name} - {hall_percentage:.2f}% full.")
    tickets_sold = 0
    command = input()
kids = kids_tickets / combine_tickets * 100
standard = standard_tickets / combine_tickets * 100
student = student_tickets / combine_tickets * 100
print(f"Total tickets: {combine_tickets}")
print(f"{student:.2f}% student tickets.")
print(f"{standard:.2f}% standard tickets.")
print(f"{kids:.2f}% kids tickets.")
