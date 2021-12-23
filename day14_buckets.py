from collections import defaultdict
polymer = []
polymerPairs = defaultdict(int)
recipes = {}
with open("day14_input.txt") as f:
    rawRows = f.readlines()
    polymer = list(rawRows[0].strip())
    for i in range(len(polymer) - 1):
        polymerPairs[polymer[i] + polymer[i+1]] += 1
    for line in rawRows[2:]:
        (left, right) = line.strip().split(" -> ")
        recipes[left] = right

def iteratePolymer(pairs, letters):
    newPairs = defaultdict(int)
    for key, count in pairs.items():
        letters[recipes[key]] += count
        newPairs[key[0] + recipes[key]] += count
        newPairs[recipes[key] + key[1]] += count
    return newPairs

letters = defaultdict(int)
for (letter1) in polymer:
    letters[letter1] += 1
for step in range(40):
    polymerPairs = iteratePolymer(polymerPairs, letters)
    #print("Step ", step, "".join(polymer))
    print("Step ", step)

counts = defaultdict(int)
for pair, count in polymerPairs.items():
    counts[pair[0]] += count

counts = letters
counts = dict(sorted(counts.items(), key=lambda item: item[1]))
print("Answer: ", counts, counts[list(counts.keys())[-1]] - (counts[list(counts.keys())[0]]))
