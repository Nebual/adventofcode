import math, sys
from copy import copy, deepcopy

class Bug:
    #nextId = 0
    COSTS = {
        'a': 1,
        'b': 10,
        'c': 100,
        'd': 1000,
    }
    def __init__(self, letter: str, hasMoved=False) -> None:
        # if id == None:
            # id = Bug.nextId
            # Bug.nextId += 1
        self.letter = letter
        # self.id = id
        self.hasMoved = hasMoved
    def __deepcopy__(self, memo):
        result = Bug(self.letter, self.hasMoved)
        memo[id(self)] = result
        return result
    def getCost(self):
        return Bug.COSTS[self.letter]
    

#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########

class Layout:
    BASE = """
#############
#...........#
###.#.#.#.###
  #.#.#.#.#
  #########
""".strip()
    ROOMS = ['room_a1','room_a2','room_b1','room_b2','room_c1','room_c2','room_d1','room_d2']
    HALLS = ['hall_ll', 'hall_l', 'hall_ab', 'hall_bc', 'hall_cd', 'hall_r', 'hall_rr']
    PATHS = [
        [
            "hall_ll", "hall_l", "hall_a", "hall_ab", "hall_b", "hall_bc",
            "hall_c", "hall_cd", "hall_d", "hall_r", "hall_rr"
        ],
        [
            "hall_ll", "hall_l", "hall_a", "hall_ab", "hall_b", "hall_bc",
            "hall_c", "hall_cd", "hall_d", "room_d1", "room_d2"
        ],
        [
            "hall_ll", "hall_l", "hall_a", "hall_ab", "hall_b", "hall_bc",
            "hall_c", "room_c1", "room_c2"
        ],
        [
            "hall_ll", "hall_l", "hall_a", "hall_ab", "hall_b", "room_b1", "room_b2"
        ],
        [
            "hall_ll", "hall_l", "hall_a", "room_a1", "room_a2"
        ],


        [
            "room_a2", "room_a1", "hall_a", "hall_ab", "hall_b", "hall_bc",
            "hall_c", "hall_cd", "hall_d", "hall_r", "hall_rr"
        ],
        [
            "room_b2", "room_b1", "hall_b", "hall_bc",
            "hall_c", "hall_cd", "hall_d", "hall_r", "hall_rr"
        ],
        [
            "room_c2", "room_c1", "hall_c", "hall_cd", "hall_d", "hall_r", "hall_rr"
        ],
        [
            "room_d2", "room_d1", "hall_d", "hall_r", "hall_rr"
        ],

        [
            "room_a2", "room_a1", "hall_a", "hall_ab", "hall_b", "hall_bc",
            "hall_c", "hall_cd", "hall_d", "room_d1", "room_d2"
        ],
        [
            "room_a2", "room_a1", "hall_a", "hall_ab", "hall_b", "hall_bc",
            "hall_c", "room_c1", "room_c2"
        ],
        [
            "room_a2", "room_a1", "hall_a", "hall_ab", "hall_b", "room_b1", "room_b2"
        ],
        [
            "room_b2", "room_b1", "hall_b", "hall_bc",
            "hall_c", "hall_cd", "hall_d", "room_d1", "room_d2"
        ],
        [
            "room_b2", "room_b1", "hall_b", "hall_bc",
            "hall_c", "room_c1", "room_c2"
        ],
        [
            "room_c2", "room_c1", "hall_c", "hall_cd",
            "hall_d", "room_d1", "room_d2"
        ],
    ]
    def __init__(self, lines) -> None:
        self.spots = {
            'room_a1': self.parseCell(lines[2][3]),
            'room_a2': self.parseCell(lines[3][3]),
            'room_b1': self.parseCell(lines[2][5]),
            'room_b2': self.parseCell(lines[3][5]),
            'room_c1': self.parseCell(lines[2][7]),
            'room_c2': self.parseCell(lines[3][7]),
            'room_d1': self.parseCell(lines[2][9]),
            'room_d2': self.parseCell(lines[3][9]),
            'hall_ll' : self.parseCell(lines[1][1]),
            'hall_l' : self.parseCell(lines[1][2]),
            'hall_ab' : self.parseCell(lines[1][4]),
            'hall_bc' : self.parseCell(lines[1][6]),
            'hall_cd' : self.parseCell(lines[1][8]),
            'hall_r' : self.parseCell(lines[1][10]),
            'hall_rr' : self.parseCell(lines[1][11]),
        }
    def printout(self, spots):
        s = [list(line) for line in Layout.BASE.splitlines()]
        for i, spot in enumerate([
            "hall_ll", "hall_l", "hall_a", "hall_ab", "hall_b", "hall_bc",
            "hall_c", "hall_cd", "hall_d", "hall_r", "hall_rr"
        ]):
            s[1][i+1] = spots[spot].letter if spot in spots and spots[spot] else '.'
        s[2][3] = spots['room_a1'].letter if 'room_a1' in spots and spots['room_a1'] else '.'
        s[3][3] = spots['room_a2'].letter if 'room_a2' in spots and spots['room_a2'] else '.'
        s[2][5] = spots['room_b1'].letter if 'room_b1' in spots and spots['room_b1'] else '.'
        s[3][5] = spots['room_b2'].letter if 'room_b2' in spots and spots['room_b2'] else '.'
        s[2][7] = spots['room_c1'].letter if 'room_c1' in spots and spots['room_c1'] else '.'
        s[3][7] = spots['room_c2'].letter if 'room_c2' in spots and spots['room_c2'] else '.'
        s[2][9] = spots['room_d1'].letter if 'room_d1' in spots and spots['room_d1'] else '.'
        s[3][9] = spots['room_d2'].letter if 'room_d2' in spots and spots['room_d2'] else '.'
        return "\n".join(["".join(row) for row in s])
    def parseCell(self, char):
        if char in ['A', 'B', 'C', 'D']:
            return Bug(char.lower())
        return ''
    def isDone(self, spots):
        for room in Layout.ROOMS:
            if not spots[room] or spots[room].letter != room[5]:
                return False
        return True
    def getPart1(self):
        return self.runSim(self.spots)
    def runSim(self, spots, energy = 0):
        bestEnergy = 999999999
        if self.isDone(spots):
            return energy
        for spot, bug in spots.items():
            if not bug: continue
            if spot[0:6] == 'room_' + bug.letter: # in right room
                if spot[-1] == '2':
                    # del spots[spot]
                    continue # in correct room bottom
                correctRoom2 = f"room_{bug.letter}2"
                if spots[correctRoom2] and spots[correctRoom2].letter == bug.letter:
                    # del spots[spot]
                    continue # in correct room top, and bottom is ok too
            # try moving it to a valid location
            for destSpot, destBug in spots.items():
                if destBug:
                    continue # full
                if bug.hasMoved and destSpot[0:4] == "hall":
                    continue # can't move in halls twice
                if destSpot[0:4] == "room" and destSpot[5] != bug.letter:
                    continue # wrong room
                # fork and move
                steps = self.canTravelTo(spots, spot, destSpot)
                if steps == -1:
                    continue # invalid move

                forkedSpots = deepcopy(spots)
                forkedSpots[destSpot] = forkedSpots[spot]
                forkedSpots[spot] = ''
                forkedSpots[destSpot].hasMoved = True
                pathEnergy = self.runSim(forkedSpots, energy + steps*bug.getCost())
                if pathEnergy < bestEnergy:
                    bestEnergy = pathEnergy
                if energy == 0:
                    print("Explored starting move", spot, "->", destSpot,":", pathEnergy)
            if energy == 0:
                print("Explored starting moves", spot)
        return bestEnergy
    
    def canTravelTo(self, spots, spot: str, destSpot: str) -> int:
        for path in Layout.PATHS:
            if spot not in path or destSpot not in path:
                continue
            # Found a path
            i1 = path.index(spot)
            i2 = path.index(destSpot)
            steps = 1
            for i in range(min(i1, i2) + 1, max(i1, i2)):
                tempSpot = path[i]
                if tempSpot in spots and spots[tempSpot]:
                    return -1
                steps += 1
            return steps
        return -1 # not a valid path?? probably unreachable

def assertSame(a, b):
    if a != b:
        print("Test failed!", a, "!=", b)
        sys.exit(1)
    else:
        print("Test passed:", a, "==", b)

test_input = """
#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########
""".strip().splitlines()
assertSame(Layout(test_input).getPart1(), 0)

test_input = """
#############
#A..........#
###.#B#C#D###
  #A#B#C#D#
  #########
""".strip().splitlines()
assertSame(Layout(test_input).getPart1(), 3)

test_input = """
#############
#...........#
###B#A#C#D###
  #A#B#C#D#
  #########
""".strip().splitlines()
assertSame(Layout(test_input).getPart1(), 46)

test_input = """
#############
#...........#
###A#B#C#D###
  #B#A#C#D#
  #########
""".strip().splitlines()
assertSame(Layout(test_input).getPart1(), 112)

test_input = """
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
""".strip().splitlines()
#assertSame(Layout(test_input).getPart1(), 12521)

part1_input = """
#############
#...........#
###B#B#D#D###
  #C#C#A#A#
  #########
""".strip().splitlines()
print("Part1:", Layout(part1_input).getPart1())
