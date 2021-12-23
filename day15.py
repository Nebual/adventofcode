DO_PART2 = True
spots = dict()
matrix = []
with open("day15_input.txt") as f:
    rawRows = f.readlines()
    height = len(rawRows)
    for yi in range(DO_PART2 and 5 or 1):
        for y, line in enumerate(rawRows):
            row = []
            rawRow = list(line.strip())
            width = len(rawRow)
            for i in range(DO_PART2 and 5 or 1):
                for x, spot in enumerate(rawRow):
                    weight = ((int(spot) + i + yi - 1) % 9) + 1
                    x2 = x + i * width
                    y2 = y + yi * height
                    spots[f"{y2}_{x2}"] = weight
                    row.append(weight)

            matrix.append(row)

from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

grid = Grid(matrix=matrix)

start = grid.node(0, 0)
end = grid.node(len(matrix[0]) - 1, len(matrix) - 1)

finder = AStarFinder()
path, runs = finder.find_path(start, end, grid)

print('operations:', runs, 'path length:', len(path), path)
#print(grid.grid_str(path=path, start=start, end=end))

sum = 0
for x,y in path[1:]:
    sum += spots[f"{y}_{x}"]
print("Answer: ", sum)
