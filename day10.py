matches = {
    "{": "}",
    "[": "]",
    "<": ">",
    "(": ")",
}
completionScoreLookup  = {
    "}": 3,
    "]": 2,
    ">": 4,
    ")": 1,
}

errors = dict()
fixScores = []
with open("day10_input.txt") as f:
    for line in f:
        stack = []
        corrupted = False
        for l in line.strip():
            if l in "{[<(":
                stack.append(l)
            elif l == matches[stack[-1]]:
                stack.pop()
            else:
                errors[l] = errors.get(l, 0) + 1
                corrupted = True
                break
        if not corrupted:
            score = 0
            for opening in reversed(stack):
                score *= 5
                score += completionScoreLookup[matches[opening]]
            fixScores.append(score)

total = errors.get("}", 0) * 1197 \
    + errors.get("]", 0) * 57 \
    + errors.get(">", 0) * 25137 \
    + errors.get(")", 0) * 3

print("Part 1 answer: ", total)

fixScores.sort()
print("Part 2 answer: ", fixScores[len(fixScores) // 2])