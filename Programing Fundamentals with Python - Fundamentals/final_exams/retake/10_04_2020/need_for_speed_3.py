number_of_cars = int(input())

cars_milage = {}
cars_fuel = {}

for vehichle in range(number_of_cars):
    car_info = input().split("|")
    car = car_info[0]
    milage = int(car_info[1])
    fuel_available = int(car_info[2])
    cars_milage[car] = milage
    cars_fuel[car] = fuel_available
command = input()
while command != "Stop":
    current_action = command.split(" : ")
    action = current_action[0]
    car = current_action[1]
    if action == "Drive":
        distance = int(current_action[2])
        fuel = int(current_action[3])
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        cars_fuel[car] -= fuel
    elif action == "Refuel":
        fuel = current_action[2]
        pass
    elif action == "Revert":
        kilometers = current_action[2]
        pass
    command = input()