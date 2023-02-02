def first_validation(password):
    if 6 <= len(password) <= 10:
        return True
    print("Password must be between 6 and 10 characters")
    return False


def second_validation(password):
    if not password.isalnum():
        return True
    print("Password must consist only of letters and digits")
    return False


def third_validation(password):
    digits = 0
    for digit in password:
        if digit.isdigit():
            digits += 1
        if digits >= 2:
            return True
        print("Password must have at least 2 digits")
        return False


password = input()

if first_validation(password) and second_validation(password) and third_validation(password):
    print("Password is valid")
elif first_validation(password):
    pass
elif second_validation(password):
    pass
elif third_validation(password):
    pass
