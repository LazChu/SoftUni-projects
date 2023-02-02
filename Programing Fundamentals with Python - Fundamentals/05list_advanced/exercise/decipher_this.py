# def decode(word: str):
#     ascii_index = int(''.join([x for x in word if x.isnumeric()]))
#     ascii_symbol = chr(ascii_index)
#     new_word = word.replace(str(ascii_index), ascii_symbol)
#     word_list = list(new_word)
#     word_list[1], word_list[-1] = word_list[-1], word_list[1]
#     decoded_word = ''.join(word_list)
#     return decoded_word
#
#
# coded_list = input().split()
# decoded_list = list()
# for word in coded_list:
#     decoded_list.append(decode(word))
#
# print(*decoded_list, sep=' ')


messages = input().split()
final_message = []
for message in messages:
    number = ""
    current_message = ""
    for character in message:
        if character.isdigit():
            number += character
        else:
            break
    message = message.replace(number, '')
    number = int(number)
    current_message += chr(number)
    if len(message) >= 2:
        message = message[-1] + message[1:-1] + message[0]
    current_message += message
    final_message.append(current_message)
print(" ".join(final_message))
