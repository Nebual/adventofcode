part1Count = 0
with open("day8_input.txt") as f:
    for line in f:
        (tenSegments, fourNumbers) = [nums.strip().split(" ") for nums in line.split(" | ")]
        if len(fourNumbers[0]) in (2, 3, 4, 7):
            part1Count += 1
        if len(fourNumbers[1]) in (2, 3, 4, 7):
            part1Count += 1
        if len(fourNumbers[2]) in (2, 3, 4, 7):
            part1Count += 1
        if len(fourNumbers[3]) in (2, 3, 4, 7):
            part1Count += 1
print("Part1: ", part1Count)
