message = input()
command = input()
while not command == "Reveal":
    instructions = command.split(":|:")
    action = instructions[0]
    if action == "InsertSpace":
        index = int(instructions[1])
        message = message[:index] + " " + message[index:]
    elif action == "Reverse":
        substring = instructions[1]
        if substring in message:
            changed_string = substring[::-1]
            message = message.replace(substring, '', 1)
            message = message + changed_string
        else:
            print("error")
            command = input()
            continue
    elif action == "ChangeAll":
        substring = instructions[1]
        replacemant = instructions[2]
        if substring in message:
            message = message.replace(substring, replacemant)
    print(message)
    command = input()
print(f"You have a new text message: {message}")
