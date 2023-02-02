number_of_letters = int(input())

for first in range(number_of_letters):
    for second in range(number_of_letters):
        for third in range(number_of_letters):
            first_letter = chr(97 + first)
            second_letter = chr(97 + second)
            third_letter = chr(97 + third)
            print(first_letter,second_letter,third_letter)