import math

class Pair:
    def __init__(self, pair, parent=None, depth=0):
        self.l, self.r = pair
        self.parent = parent
        self.depth = depth
        if type(self.l) == list:
            self.l = Pair(self.l, self, depth + 1)
        elif isinstance(self.l, Pair):
            self.l.adjustDepth(1, self)
        if type(self.r) == list:
            self.r = Pair(self.r, self, depth + 1)
        elif isinstance(self.r, Pair):
            self.r.adjustDepth(1, self)
    def adjustDepth(self, amount, newParent=None):
        self.depth += amount
        if self.depth == 0:
            self.parent = None
        else:
            self.parent = newParent
        if isinstance(self.l, Pair):
            self.l.adjustDepth(amount, self)
        if isinstance(self.r, Pair):
            self.r.adjustDepth(amount, self)
        return self
    def reduceFully(self):
        while not self.reduce(False):
            pass
        while not self.reduce(True):
            pass
    def reduce(self, secondPass=False):
        if self.depth >= 4:
            self.parent.explodeAddLeft(self.l, self)
            self.parent.explodeAddRight(self.r, self)
            if self.parent.l == self:
                self.parent.l = 0
            else:
                self.parent.r = 0
            return False
        if isinstance(self.l, Pair):
            if not self.l.reduce(secondPass):
                return False
        if secondPass and (type(self.l) == int and self.l > 9):
            num = self.l
            self.l = Pair([int(math.floor(num / 2.0)), int(math.ceil(num / 2.0))], self, self.depth + 1)
            return False
        if isinstance(self.r, Pair):
            if not self.r.reduce(secondPass):
                return False
        if secondPass and type(self.r) == int and self.r > 9:
            num = self.r
            self.r = Pair([int(math.floor(num / 2.0)), int(math.ceil(num / 2.0))], self, self.depth + 1)
            return False
        return True
    def explodeAddLeft(self, num, skip):
        if self.l == skip:
            if self.parent is None:
                return # do nothing
            self.parent.explodeAddLeft(num, self)
        else:
            if self.r == skip:
                if isinstance(self.l, Pair):
                    self.l.addRight(num)
                else:
                    self.l += num
            elif isinstance(self.r, Pair):
                self.r.addRight(num)
            else:
                self.r += num
    def explodeAddRight(self, num, skip):
        if self.r == skip:
            if self.parent is None:
                return # do nothing
            self.parent.explodeAddRight(num, self)
        else:
            if self.l == skip:
                if isinstance(self.r, Pair):
                    self.r.addLeft(num)
                else:
                    self.r += num
            elif isinstance(self.l, Pair):
                self.l.addLeft(num)
            else:
                self.l += num
    def getMagnitude(self):
        left = self.l
        if isinstance(left, Pair):
            left = left.getMagnitude()
        right = self.r
        if isinstance(right, Pair):
            right = right.getMagnitude()
        return 3 * left + 2 * right
    def toList(self, withDepth=False):
        if self.parent != None:
            l = [f"{self.depth}-{self.parent.depth}-{self.l}", f"{self.depth}-{self.parent.depth}-{self.r}"] if withDepth else [self.l, self.r]
        else:
            l = [f"{self.depth}-{self.l}", f"{self.depth}-{self.r}"] if withDepth else [self.l, self.r]
        if isinstance(self.l, Pair):
            l[0] = self.l.toList(withDepth)
        if isinstance(self.r, Pair):
            l[1] = self.r.toList(withDepth)
        return l
    def __str__(self) -> str:
        return str(self.toList())
    def addLeft(self, num):
        if isinstance(self.l, Pair):
            self.l.addLeft(num)
        else:
            self.l += num
    def addRight(self, num):
        if isinstance(self.r, Pair):
            self.r.addRight(num)
        else:
            self.r += num

import sys
def assertReduction(start, finish):
    a = Pair(start)
    a.reduceFully()
    if a.toList() != finish:
        print("Test failed!", a.toList(), "!=", finish)
        sys.exit(1)

assertReduction([[[[[9,8],1],2],3],4], [[[[0,9],2],3],4])
assertReduction([7,[6,[5,[4,[3,2]]]]], [7,[6,[5,[7,0]]]])
assertReduction([[6,[5,[4,[3,2]]]],1], [[6,[5,[7,0]]],3])
assertReduction([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]], [[3,[2,[8,0]]],[9,[5,[7,0]]]])

assertReduction([[[[[4,3],4],4],[7,[[8,4],9]]], [1,1]], [[[[0,7],4],[[7,8],[6,0]]],[8,1]])
assertReduction([Pair([[[[4,3],4],4],[7,[[8,4],9]]]), Pair([1,1])], [[[[0,7],4],[[7,8],[6,0]]],[8,1]])

assertReduction([Pair([[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]), Pair([7,[[[3,7],[4,3]],[[6,3],[8,8]]]])], \
  [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]])

lines = None
with open("day18_input.txt") as f:
    lines = f.readlines()
    snailfish = eval(lines[0].strip())
    rootPair = Pair(snailfish)
    print(rootPair.toList(True))
    for i,lineRaw in enumerate(lines[1:]):
        toAdd = eval(lineRaw.strip())
        rootPair = Pair([rootPair, Pair(toAdd)])
        print(i, rootPair.toList())
       # print(rootPair.toList(True))
        rootPair.reduceFully()
        print(i, rootPair.toList())
        # snailfish = [snailfish, toAdd]
        # snailfish = reduceSnailfish(snailfish)
    print("Resulting snailfish: ", rootPair)
    print("Part1 Magnitude:", rootPair.getMagnitude())

magnitudes = []
for i1, line in enumerate(lines):
    for line2 in lines:
        if line == line2: continue
        added = Pair([eval(line.strip()), eval(line2.strip())])
        added.reduceFully()
        mag = added.getMagnitude()
        print(i1, mag)
        magnitudes.append(mag)
print("Part2:", max(magnitudes))
