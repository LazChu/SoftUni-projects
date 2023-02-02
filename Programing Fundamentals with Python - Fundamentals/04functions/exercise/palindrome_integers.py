def palindrome(num):
    for n in numbers:
        if n == n[::-1]:
            print('True')
        else:
            print('False')


numbers = input().split(', ')

palindrome(numbers)