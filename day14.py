polymer = []
recipes = {}
with open("day14_input.txt") as f:
    rawRows = f.readlines()
    polymer = list(rawRows[0].strip())
    for line in rawRows[2:]:
        (left, right) = line.strip().split(" -> ")
        recipes[left] = right

print("Step -1", "".join(polymer))
for step in range(10):
    iNew = 0
    newPolymer = polymer[:]
    for i in range(len(polymer) - 1):
        iNew += 1
        chunk = polymer[i] + polymer[i+1]
        if chunk in recipes:
            newPolymer.insert(iNew, recipes[chunk])
            iNew += 1
    polymer = newPolymer
    print("Step ", step, "".join(polymer))
    print("Step ", step)

counts = dict()
for letter in polymer:
    if letter not in counts:
        counts[letter] = 1
    else:
        counts[letter] += 1

counts = dict(sorted(counts.items(), key=lambda item: item[1]))
print("Answer: ", counts, counts[list(counts.keys())[-1]] - counts[list(counts.keys())[0]])
