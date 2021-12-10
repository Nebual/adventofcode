numberOrder = None
boards = []
markedBoards = []
with open("day4_input.txt") as f:
    lines = f.readlines()
    numberOrder = lines[0].split(',')
    partialBoard = []
    for line in lines[2:]:
        line = line.strip()
        if line:
            for x in line.replace('  ', ' ').split(' '):
                partialBoard.append(int(x.strip()))
        else:
            boards.append(partialBoard)
            markedBoards.append(dict())
            partialBoard = []

def checkBoardWins(markedBoard):
    for r in (range(0,5), range(5, 10), range(10, 15), range(15, 20), range(20, 25),
            range(0,25,5), range(1,25,5), range(2,25,5), range(3,25,5), range(4,25,5)):
        allTrue = True
        for i in r:
            if i not in markedBoard:
                allTrue = False
                break
        if allTrue:
            return True
    return False
def calculateBoardScore(board, markedBoard, drawn):
    sum = 0
    for i, num in enumerate(board):
        if i not in markedBoard:
            sum += num
    return sum * drawn



victoryBoards = dict()
for drawn in numberOrder:
    drawn = int(drawn)
    for boardIndex, board in enumerate(boards):
        if boardIndex in victoryBoards:
            continue
        try:
            index = board.index(drawn)
            markedBoards[boardIndex][index] = True
            if checkBoardWins(markedBoards[boardIndex]):
                if not len(victoryBoards.keys()):
                    print("Part1 Answer: ", calculateBoardScore(board, markedBoards[boardIndex], drawn))
                victoryBoards[boardIndex] = True
                if len(victoryBoards.keys()) == len(boards):
                    print("Part2 Answer: ", calculateBoardScore(board, markedBoards[boardIndex], drawn))
        except ValueError:
            pass
