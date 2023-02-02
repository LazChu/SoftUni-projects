number_bad_scores = int(input())


total_score = 0
assigments = 0
bad_scores = 0
last_assigment = ''
while number_bad_scores > bad_scores:
    assignment = input()
    if assignment == 'Enough':
        break
    score = int(input())
    if score <= 4:
        bad_scores += 1
    total_score += score
    assigments += 1
    last_assigment = assignment
avg_score = total_score / assigments
if assignment == 'Enough':
    print(f"Average score: {avg_score:.2f}")
    print(f"Number of problems: {assigments}")
    print(f"Last problem: {last_assigment}")
if number_bad_scores == bad_scores:
    print(f"You need a break, {bad_scores} poor grades.")