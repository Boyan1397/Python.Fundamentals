cards = input().split()
n = int(input())

half_deck = len(cards) // 2
for i in range(n):
    left_side = cards[0:half_deck]
    right_side = cards[half_deck:]

    shuffled_cards = []

    for index in range(len(left_side)):
        shuffled_cards.append(left_side[index])
        shuffled_cards.append(right_side[index])

    cards = shuffled_cards

print(cards)


