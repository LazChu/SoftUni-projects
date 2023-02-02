from math import ceil

number_of_students = int(input())
total_lectures = int(input())
aditional_bonus = int(input())
current_attendancies = 0
current_bonus = 0
for student in range(number_of_students):
    attendances = int(input())
    total_bonus = attendances / total_lectures * (5 + (aditional_bonus))
    if total_bonus > current_bonus:
        current_bonus = total_bonus
        current_attendancies = attendances

print(f"Max Bonus: {ceil(current_bonus)}.")
print(f"The student has attended {current_attendancies} lectures.")
