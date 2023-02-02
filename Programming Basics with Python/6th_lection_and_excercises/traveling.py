destination = input()


while destination != 'End':
    destination = destination
    budget = float(input())
    current_budget = 0
    while current_budget < budget:
        amount = float(input())
        current_budget += amount
    if current_budget >= budget:
        print(f"Going to {destination}!")
    destination = input()
