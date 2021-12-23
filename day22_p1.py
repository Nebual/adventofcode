import math, re, sys

def checkValidity(numbers):
    for i in range(0, 6, 2):
        if numbers[i] < -50 and numbers[i+1] < -50:
            return False
        if numbers[i] > 50 and numbers[i+1] > 50:
            return False
    return True


def parseLines(f):
    grid = {}
    for line in f:
        matches = re.match(r"(on|off) x=([-\d]+)\.\.([-\d]+),y=([-\d]+)\.\.([-\d]+),z=([-\d]+)\.\.([-\d]+)", line)
        on = matches.groups()[0] == "on"
        numbers = [int(x) for x in matches.groups()[1:]]
        if not checkValidity(numbers):
            continue

        [xStart, xEnd, yStart, yEnd, zStart, zEnd] = [max(-50, min(50, x)) for x in numbers]
        for x in range(xStart, xEnd + 1):
            for y in range(yStart, yEnd + 1):
                for z in range(zStart, zEnd + 1):
                    if on:
                        grid[f"{x}_{y}_{z}"] = True
                    else:
                        try:
                            del grid[f"{x}_{y}_{z}"]
                        except KeyError:
                            pass
    return grid

testCase1 = """
on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10
""".strip()
testResult1 = parseLines(testCase1.split("\n"))
def assertSame(a, b):
    if a != b:
        print("Test failed!", a, "!=", b)
        sys.exit(1)
assertSame(len(testResult1.keys()), 39)

with open("day22_input_test2.txt") as f:
    assertSame(len(parseLines(f).keys()), 590784)

with open("day22_input.txt") as f:
    grid = parseLines(f)
    print("Part1 answer:", len(grid.keys()))
