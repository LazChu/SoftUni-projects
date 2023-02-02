number = int(input())

for i in range(number):
    code = int(input())
    if code == 88:
        greeting = 'Hello'
    elif code == 86:
        greeting = 'How are you?'
    elif code < 88:
        greeting = 'GREAT!'
    elif code > 88:
        greeting = 'Bye.'
    print(greeting)