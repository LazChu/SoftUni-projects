student = input()

years = 1
sum_grades = 0
failed_years = 0

while years <= 12:
    if failed_years >= 2:
        break
    degree = float(input())
    if degree < 4:
        failed_years += 1
        continue
    years += 1
    sum_grades += degree
average_degree = sum_grades / 12
if failed_years == 2:
    print(f"{student} has been excluded at {years} grade")
else:
    print(f"{student} graduated. Average grade: {average_degree:.2f}")