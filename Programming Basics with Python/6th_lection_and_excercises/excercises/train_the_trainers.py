jury_number = int(input())
command = input()
total_presentation_score = 0
tasks = 0
combine_score = 0
total_score = 0
while command != 'Finish':
    presentation = command

    for score in range(jury_number):
        presentation_score = float(input())
        total_presentation_score += presentation_score
        tasks += 1
        combine_score += presentation_score
    avg_score = total_presentation_score / jury_number

    print(f"{presentation} - {avg_score:.2f}.")
    total_presentation_score = 0
    total_score = combine_score / tasks
    command = input()
if command == 'Finish':
    print(f"Student's final assessment is {total_score:.2f}.")