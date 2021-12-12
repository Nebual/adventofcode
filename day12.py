connections = dict()
with open("day12_input.txt") as f:
    for pair in f:
        (first, second) = pair.strip().split("-")
        if first not in connections: connections[first] = []
        if second not in connections: connections[second] = []
        connections[first].append(second)
        connections[second].append(first)

allPaths = set()
def traverse(path, cave, allowDoubleVisit=False):
    global allPaths
    if cave == "start":
        return 0
    if cave == "end":
        path.append(cave)
        allPaths.add(','.join([str(x) for x in path]))
        return len(path)
    if cave.lower() == cave and cave in path:
        if allowDoubleVisit:
            allowDoubleVisit = False
        else:
            return 0
    
    path.append(cave)
    for newCave in connections[cave]:
        traverse(path[:], newCave, allowDoubleVisit)

path = ["start"]
for newCave in connections["start"]:
    traverse(path[:], newCave)
print("Part 1 answer: ", len(allPaths))

# allPaths = list(allPaths)
# allPaths.sort()
# for path in allPaths:
#     print(path)

for newCave in connections["start"]:
    traverse(path[:], newCave, True)
print("Part 2 answer: ", len(allPaths))
