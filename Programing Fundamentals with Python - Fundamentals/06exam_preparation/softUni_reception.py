first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students = int(input())

time_needed = first_employee + second_employee + third_employee

hours = 0
while students > 0:
    students -= time_needed
    hours += 1
    if hours % 4 == 0:
        hours += 1
print(f"Time needed: {hours}h.")
