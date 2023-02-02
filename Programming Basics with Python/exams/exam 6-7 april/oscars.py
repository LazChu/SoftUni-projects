rent_hall = int(input())

oscars = rent_hall * 0.70
catering = oscars * 0.85
sound_stage = catering / 2

total_expenses = rent_hall + oscars + catering + sound_stage

print(f'{total_expenses:.2f}')
