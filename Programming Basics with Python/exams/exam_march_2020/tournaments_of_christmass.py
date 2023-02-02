days_of_tournament = int(input())

wins = 0
total_wins = 0
loses = 0
total_loses = 0
money = 0
total_money = 0

for days in range(days_of_tournament):
    command = input()
    wins = 0
    loses = 0
    money = 0
    while command != 'Finish':
        sport = command
        result = input()
        if result == 'win':
            money += 20
            wins += 1
        else:
            loses += 1
        command = input()
    if wins > loses:
        money += (money * 0.10)
    total_money += money
    total_wins += wins
    total_loses += loses
if total_wins > total_loses:
    total_money += (total_money * 0.20)
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
