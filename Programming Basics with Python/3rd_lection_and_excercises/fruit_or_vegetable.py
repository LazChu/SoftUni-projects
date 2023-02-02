name = input()

fruits = name == 'banana' or name == 'apple' or name == 'kiwi' or name == 'cherry' \
         or name == 'lemon' or name == 'grapes'
vegetables = name == 'tomato' or name == 'cucumber' or name == 'pepper' or name == 'carrot'

if fruits:
    print('fruit')
elif vegetables:
    print('vegetable')
else:
    print('unknown')