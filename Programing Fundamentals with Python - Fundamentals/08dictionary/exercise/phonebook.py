command = input()
phonebook = {}
while "-" in command:
    contact_info = command.split("-")
    name = contact_info[0]
    number = contact_info[1]
    if name not in phonebook:
        phonebook[name] = 0
    phonebook[name] = number
    command = input()
for search in range(int(command)):
    contact = input()
    if contact in phonebook:
        print(f"{contact} -> {phonebook[contact]}")
    else:
        print(f"Contact {contact} does not exist.")
