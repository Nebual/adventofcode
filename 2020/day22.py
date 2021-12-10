with open("2020/day22.txt") as f:
    [deck1, deck2] = f.read().split("Player 2:")
deck1 = [int(x) for x in deck1.strip().splitlines()[1:]]
deck2 = [int(x) for x in deck2.strip().splitlines()]

while len(deck1) > 0 and len(deck2) > 0:
    card1 = deck1.pop(0)
    card2 = deck2.pop(0)
    if card1 > card2:
        deck1.append(card1)
        deck1.append(card2)
    else:
        deck2.append(card2)
        deck2.append(card1)

def calcScore(deck):
    sum = 0
    for i, card in enumerate(reversed(deck)):
        sum += (i+1) * card
    return sum
print("Scores:", calcScore(deck1), "other", calcScore(deck2))
