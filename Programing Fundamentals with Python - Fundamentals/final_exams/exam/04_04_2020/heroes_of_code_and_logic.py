number_of_heroes = int(input())
heroes = {}
for hero_number in range(number_of_heroes):
    data = input().split()
    name = data[0]
    health = int(data[1])
    mana = int(data[2])
    heroes[name] = {'health': health, 'mana': mana}

command = input()
while command != "End":
    current_action = command.split(" - ")
    action = current_action[0]
    name = current_action[1]
    if action == "CastSpell":
        mana_needed = int(current_action[2])
        spell_name = current_action[3]
        if heroes[name]['mana'] >= mana_needed:
            heroes[name]['mana'] -= mana_needed
            print(f"{name} has successfully cast {spell_name} and now has {heroes[name]['mana']} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")
    elif action == "TakeDamage":
        damage = int(current_action[2])
        attacker = current_action[3]
        heroes[name]['health'] -= damage
        if heroes[name]['health'] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name]['health']} HP left!")
        else:
            print(f"{name} has been killed by {attacker}!")
            heroes.pop(name)
    elif action == "Recharge":
        amount = int(current_action[2])
        if heroes[name]['mana'] + amount >= 200:
            current_amount = 200 - heroes[name]['mana']
            print(f"{name} recharged for {current_amount} MP!")
            heroes[name]['mana'] = 200
        else:
            heroes[name]['mana'] += amount
            print(f"{name} recharged for {amount} MP!")
    elif action == "Heal":
        amount = int(current_action[2])
        if heroes[name]['health'] + amount >= 100:
            current_amount = 100 - heroes[name]['health']
            print(f"{name} healed for {current_amount} HP!")
            heroes[name]['health'] = 100
        else:
            heroes[name]['health'] += amount
            print(f"{name} healed for {amount} HP!")
    command = input()

for hero in heroes:
    print(hero)
    print(f"  HP: {heroes[hero]['health']}")
    print(f"  MP: {heroes[hero]['mana']}")
