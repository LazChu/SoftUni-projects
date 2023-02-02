command = input()
students = {}
while ":" in command:
    student_info = command.split(":")
    name = student_info[0]
    student_id = student_info[1]
    course = student_info[2]
    if course not in students:
        students[course] = {}
    students[course][student_id] = name
    command = input()
searched_students = {}
searched = command.split("_")
searched_course = " ".join(searched)
for course in students.keys():
    if searched_course == course:
        searched_students = students[course]

for key,value in searched_students.items():
    print(f"{value} - {key}")
