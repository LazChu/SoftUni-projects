cards = input().split(' ')
faro_shuffles = int(input())

decks_length = len(cards) // 2


for shuffles in range(faro_shuffles):
    shuffled_deck = []
    left_deck = cards[:decks_length]
    right_deck = cards[decks_length:]
    for card in range(len(left_deck)):
        shuffled_deck.append(left_deck[card])
        shuffled_deck.append(right_deck[card])
    cards = shuffled_deck
print(cards)