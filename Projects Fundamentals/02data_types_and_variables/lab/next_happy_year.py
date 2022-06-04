year = int(input())
year_as_string = str(year)
happy_year = ''
for digit in (year_as_string):
    single_digit = digit
    if single_digit != digit:
        happy_year += digit

print(happy_year)
