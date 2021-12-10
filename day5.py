DO_PART2 = True

board = dict()
with open("day5_input.txt") as f:
    for line in f:
        (start, end) = line.split(' -> ')
        (xStart, yStart) = start.split(',') 
        (xEnd, yEnd) = end.split(',')
        xStart = int(xStart)
        yStart = int(yStart)
        xEnd = int(xEnd)
        yEnd = int(yEnd)
        xMin = min(xStart, xEnd)
        xMax = max(xStart, xEnd)
        yMin = min(yStart, yEnd)
        yMax = max(yStart, yEnd)

        if yStart == yEnd: # horizontal
            for x in range(xMin, xMax + 1):
                if x not in board:
                    board[x] = dict()
                if yStart not in board[x]:
                    board[x][yStart] = 0
                board[x][yStart] += 1
        elif xStart == xEnd: # vertical
            for y in range(yMin, yMax + 1):
                if xStart not in board:
                    board[xStart] = dict()
                if y not in board[xStart]:
                    board[xStart][y] = 0
                board[xStart][y] += 1
        elif DO_PART2: # diagonal
            xSign = (xStart - xEnd) > 0 and -1 or 1
            ySign = (yStart - yEnd) > 0 and -1 or 1
            y = yStart - ySign
            for x in range(xStart, xEnd + xSign, xSign):
                y += ySign
                if x not in board:
                    board[x] = dict()
                if y not in board[x]:
                    board[x][y] = 0
                board[x][y] += 1

count = 0
for column in board.values():
    for cell in column.values():
        if cell >= 2:
            count += 1

print("Answer: ", count)