#Read User Input
card_deck = input().split()
shuffles = int(input())

#Logic

left_part = []
right_part = []

for i in range(shuffles):
    split = len(card_deck) // 2
    left_part = card_deck[0:split]
    right_part = card_deck[split:]
    shuffled_deck = []
    for j in range(len(left_part)):
        shuffled_deck.append(left_part[j])
        shuffled_deck.append(right_part[j])
    card_deck = shuffled_deck

#Print Output

print(card_deck)