activation_key = input()
command = input()
while command != "Generate":
    action = command.split(">>>")
    current_action = action[0]
    if current_action == "Contains":
        substring = action[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print('Substring not found!')
    elif current_action == "Flip":
        case_manipulation = action[1]
        start = int(action[2])
        end = int(action[3])
        if case_manipulation == "Lower":
            lower_cases = activation_key[start:end].lower()
            activation_key = activation_key[:start] + lower_cases + activation_key[end:]
        elif case_manipulation == "Upper":
            upper_cases = activation_key[start:end].upper()
            activation_key = activation_key[:start] + upper_cases + activation_key[end:]
        print(activation_key)
    elif current_action == "Slice":
        start = int(action[1])
        end = int(action[2])
        activation_key = activation_key[:start] + activation_key[end:]
        print(activation_key)
    command = input()
print(f"Your activation key is: {activation_key}")