open_tabs = int(input())
salary = int(input())

# "Facebook" -> 150 лв.
# "Instagram" -> 100 лв.
# "Reddit" -> 50 лв.
fine = 0

for tabs in range (open_tabs):
    website = input()
    if website == 'Facebook':
        fine += 150
    elif website == 'Instagram':
        fine += 100
    elif website == 'Reddit':
        fine += 50
    if salary <= fine:
        break
if fine >= salary:
    print("You have lost your salary.")
else:
    diff = salary - fine
    print(abs(diff))






number_open_tabs = int(input())
salary = int(input())

Facebook = 150
Instagram = 100
Reddit = 50
no_more_salary = False
for tabs in range(number_open_tabs):
    tab = input()
    if tab == 'Facebook':
        salary -= 150
    elif tab == 'Instagram':
        salary -= 100
    elif tab == 'Reddit':
        salary -= 50
    if salary <= 0:
        no_more_salary = True
        break
if no_more_salary:
    print("You have lost your salary.")
else:
    print(salary)