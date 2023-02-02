from math import ceil
persons = int(input())
elevator_capacity = int(input())

courses = persons / elevator_capacity
print(ceil(courses))