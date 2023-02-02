vacation_money = float(input())
money = float(input())

total_days = 0
spending_days = 0
spending_days_in_a_row = False

while money < vacation_money:
    total_days += 1
    action = (input())
    current_money = float(input())
    if action == 'save':
        money += current_money
        spending_days = 0
    else:
        money -= current_money
        spending_days += 1
        if spending_days >= 5:
            spending_days_in_a_row = True
            break
        if money < 0:
            money = 0
if spending_days_in_a_row:
    print("You can't save the money.")
    print(total_days)
else:
    print(f"You saved the money for {total_days} days.")