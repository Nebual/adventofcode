fish = list()
with open("day6_input.txt") as f:
    for age in f.read().strip().split(','):
        fish.append(int(age))
for day in range(256):
    if day == 80:
        print("Part1 Answer: ", len(fish))

    newFish = []
    for i, age in enumerate(fish):
        if age > 0:
            newFish.append(age - 1)
        else:
            newFish.append(8)
            newFish.append(6)
    fish = newFish
    print("Day ", day + 1, ", count: ", len(fish))
print("Part2 Answer: ", len(fish))
