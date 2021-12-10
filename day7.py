crabPositions = []
with open("day7_input.txt") as f:
    crabPositions = [int(x) for x in f.read().split(',')]
fuels = []
fuels2 = []
def gaussSum(n):
    return (n * (n + 1)) / 2
for i in range(max(crabPositions)):
    fuels.append(
        sum([abs(i - x) for x in crabPositions])
    )
    fuels2.append(
        sum([gaussSum(abs(i - x)) for x in crabPositions])
    )
print("Part 1, Min Fuel: ", min(fuels), "position:", fuels.index(min(fuels)))
print("Part 2, Min Fuel: ", min(fuels2), "position:", fuels2.index(min(fuels2)))

import statistics
print("median", statistics.median(crabPositions), "mean", statistics.mean(crabPositions))