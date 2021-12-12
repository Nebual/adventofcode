rows = []
with open("day9_input.txt") as f:
    rows = [[int(x) for x in row.strip()] for row in f.readlines()]
width = len(rows[0])
height = len(rows)

def get(listArg, key, default):
    if key < 0 or key >= len(listArg):
        return default
    return listArg[key]

def getLowestAdjacentHeight(x, y):
    return min(
        get(get(rows, y + 1, []), x, 9),
        get(get(rows, y - 1, []), x, 9),
        get(get(rows, y, []), x + 1, 9),
        get(get(rows, y, []), x - 1, 9)
    )

def findBottom(x, y):
    height = get(get(rows, y, []), x, 9)
    lowest = getLowestAdjacentHeight(x, y)
    if height < lowest:
        return f"{x}_{y}"
    if lowest == get(get(rows, y + 1, []), x, 9):
        return findBottom(x, y + 1)
    if lowest == get(get(rows, y - 1, []), x, 9):
        return findBottom(x, y - 1)
    if lowest == get(get(rows, y, []), x + 1, 9):
        return findBottom(x + 1, y)
    if lowest == get(get(rows, y, []), x - 1, 9):
        return findBottom(x - 1, y)


lowPoints = dict()
lowPointsRisk = 0
for y, row in enumerate(rows):
    for x, height in enumerate(row):
        if height == 9: continue
        key = f"{x}_{y}"
        if height < getLowestAdjacentHeight(x, y):
            lowPoints[key] = lowPoints.get(key, 0) + 1
            lowPointsRisk += 1 + height
        else:
            key = findBottom(x, y)
            lowPoints[key] = lowPoints.get(key, 0) + 1

print("Part 1 answer: ", lowPointsRisk)

largest = list(lowPoints.values())
largest.sort(reverse=True)
largest3Multiplied = largest[0] * largest[1] * largest[2]
print("Part 2 answer: ", largest3Multiplied)


from colorama import init
init()
from blessings import Terminal
term = Terminal()

for y, row in enumerate(rows):
    for x, height in enumerate(row):
        text = str(height)
        key = f"{x}_{y}"
        if key in lowPoints:
            print(term.bold(term.standout(text)), end="")
        elif height == 9:
            print(term.black(text), end="")
        else:
            colorIndex = list(lowPoints.keys()).index(findBottom(x, y)) % term.number_of_colors
            print(term.color(colorIndex)(text), end="")
    print("")

print("Part 1 answer: ", lowPointsRisk)
print("Part 2 answer: ", largest3Multiplied)
