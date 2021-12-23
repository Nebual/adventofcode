import math, re, sys

class Cube:
    def __init__(self, on: bool, numbers) -> None:
        self.on = on
        self.xStart, self.xEnd, self.yStart, self.yEnd, self.zStart, self.zEnd = numbers
    def dupe(self):
        return Cube(self.on, self.toNumbers())
    def toNumbers(self):
        return [self.xStart, self.xEnd, self.yStart, self.yEnd, self.zStart, self.zEnd]
    def intersect(self, other: 'Cube'):
        if self.xEnd >= other.xStart and self.xStart <= other.xEnd \
            and self.yEnd >= other.yStart and self.yStart <= other.yEnd \
            and self.zEnd >= other.zStart and self.zStart <= other.zEnd:
            return True
        return False
    def volume(self):
        return (self.xEnd + 1 - self.xStart) \
            * (self.yEnd + 1 - self.yStart) \
            * (self.zEnd + 1 - self.zStart)
    def split(self, other: 'Cube'):
        # only include on cubes
        # 5 - 20 self
        # 9 - 10
        cubes = []
        if self.zStart < other.zStart:
            newCube = self.dupe()
            newCube.zEnd = other.zStart - 1
            cubes.append(newCube)
            self.zStart = other.zStart
        if self.zEnd > other.zEnd:
            newCube = self.dupe()
            newCube.zStart = other.zEnd + 1
            cubes.append(newCube)
            self.zEnd = other.zEnd
        if self.yStart < other.yStart:
            newCube = self.dupe()
            newCube.yEnd = other.yStart - 1
            #newCube.zStart = max(other.zEnd + 1, self.zStart)
            #newCube.zEnd = min(other.zStart - 1, self.zEnd)
            cubes.append(newCube)
            self.yStart = other.yStart
        if self.yEnd > other.yEnd:
            newCube = self.dupe()
            newCube.yStart = other.yEnd + 1
            #newCube.zStart = max(other.zEnd + 1, self.zStart)
            #newCube.zEnd = min(other.zStart - 1, self.zEnd)
            cubes.append(newCube)
            self.yEnd = other.yEnd
        if self.xStart < other.xStart:
            newCube = self.dupe()
            newCube.xEnd = other.xStart - 1
            #newCube.yStart = max(other.yEnd + 1, self.yStart)
            #newCube.yEnd = min(other.yStart - 1, self.yEnd)
            #newCube.zStart = max(other.zEnd + 1, self.zStart)
            #newCube.zEnd = min(other.zStart - 1, self.zEnd)
            cubes.append(newCube)
            self.xStart = other.xStart
        if self.xEnd > other.xEnd:
            newCube = self.dupe()
            newCube.xStart = other.xEnd + 1
            # newCube.yStart = max(other.yEnd + 1, self.yStart)
            # newCube.yEnd = min(other.yStart - 1, self.yEnd)
            # newCube.zStart = max(other.zEnd + 1, self.zStart)
            # newCube.zEnd = min(other.zStart - 1, self.zEnd)
            cubes.append(newCube)
            self.xEnd = other.xEnd

        return cubes


def parseLines(f):
    cubes = []
    for line in f:
        matches = re.match(r"(on|off) x=([-\d]+)\.\.([-\d]+),y=([-\d]+)\.\.([-\d]+),z=([-\d]+)\.\.([-\d]+)", line)
        on = matches.groups()[0] == "on"
        numbers = [int(x) for x in matches.groups()[1:]]
        cube = Cube(on, numbers)
        newCubes = []
        for existingCube in cubes:
            if existingCube.intersect(cube):
                newCubes += existingCube.split(cube)
            else:
                newCubes.append(existingCube)
        if cube.on:
            newCubes.append(cube)
        cubes = newCubes
        print("temp volume", len(cubes), sum([cube.volume() for cube in cubes]))
    
    return sum([cube.volume() for cube in cubes])


def assertSame(a, b):
    if a != b:
        print("Test failed!", a, "!=", b)
        sys.exit(1)

assertSame(
    parseLines([
        "on x=10..12,y=10..12,z=10..12",
        "off x=10..12,y=10..12,z=10..11"
    ]),
    9
)

assertSame(
    parseLines([
        "on x=10..12,y=10..12,z=10..12",
        "off x=10..12,y=10..12,z=11..11"
    ]),
    18
)

assertSame(
    parseLines([
        "on x=10..12,y=10..12,z=10..12",
        "off x=10..14,y=9..12,z=11..11"
    ]),
    18
)

assertSame(
    parseLines([
        "on x=10..12,y=10..12,z=10..12",
        "off x=11..11,y=11..11,z=11..11"
    ]),
    27 - 1
)

assertSame(
    parseLines([
        "on x=10..12,y=10..12,z=10..12",
        "off x=9..11,y=9..11,z=9..11",
    ]),
    27 - 8
)
assertSame(
    parseLines([
        "on x=10..12,y=10..12,z=10..12",
        "on x=11..13,y=11..13,z=11..13",
        "off x=9..11,y=9..11,z=9..11",
    ]),
    27 + 19 - 8
)
assertSame(
    parseLines([
        "on x=10..12,y=10..12,z=10..12",
        "on x=11..13,y=11..13,z=11..13",
        "off x=9..11,y=9..11,z=9..11",
        "on x=10..10,y=10..10,z=10..10"
    ]),
    39 # 27 + 19 - 8 + 1
)


# with open("day22_input_test2.txt") as f:
    # assertSame(parseLines(f), 590784)

with open("day22_input.txt") as f:
    print("Part2 answer:", parseLines(f))
