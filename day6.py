fishAges = dict()
with open("day6_input.txt") as f:
    for age in f.read().strip().split(','):
        fishAges[int(age)] = fishAges.get(int(age), 0) + 1

for day in range(256):
    if day == 80:
        print("Part1 Answer: ", sum(fishAges.values()))

    newAges = dict()
    for age, count in fishAges.items():
        if age > 0:
            newAges[age - 1] = newAges.get(age - 1, 0) + count
        else:
            newAges[6] = newAges.get(6, 0) + count
            newAges[8] = newAges.get(8, 0) + count
    fishAges = newAges
print("Part2 Answer: ", sum(fishAges.values()))
