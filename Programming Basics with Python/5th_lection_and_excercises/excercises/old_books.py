favorite_book = input()

books = 0
book = ''
while book != favorite_book:
    book = input()

    if book == favorite_book:
        continue

    if book == 'No More Books':
        break
    books += 1

if favorite_book == book:
    print(f"You checked {books} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {books} books.")




searched_book_name = input()

book = ''
books_searched = 0
book_is_found = False
while book != searched_book_name:
    book = input()
    if book == 'No More Books':
        break
    if searched_book_name == book:
        book_is_found = True
        continue
    books_searched += 1

if book_is_found:
    print(f"You checked {books_searched} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {books_searched} books.")