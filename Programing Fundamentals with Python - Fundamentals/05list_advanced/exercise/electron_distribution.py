number_of_electrons = int(input())
shells = []
electron_counter = 0
while number_of_electrons > 0:
    electron_counter += 1
    electron = 2 * electron_counter ** 2
    if electron > number_of_electrons:
        electron = number_of_electrons
    shells.append(electron)
    number_of_electrons -= electron
print(shells)