IS_PART2 = True

with open("2016/day12.txt") as f:
    instructions = [line.strip().split(" ") for line in f.readlines()]

def runProgram(startingA):
    currentLine = 0
    registers = dict()
    registers['a'] = startingA
    registers['b'] = 0
    registers['c'] = IS_PART2 and 1 or 0
    registers['d'] = 0
    lastOut = 0
    outCount = 0

    while currentLine < len(instructions):
        cmd = instructions[currentLine]
        if cmd[0] == "cpy":
            val1 = int(registers.get(cmd[1], cmd[1]))
            val2 = cmd[2]
            registers[val2] = val1
        elif cmd[0] == "inc":
            registers[cmd[1]] += 1
        elif cmd[0] == "dec":
            registers[cmd[1]] -= 1
        elif cmd[0] == "jnz":
            val1 = int(registers.get(cmd[1], cmd[1]))
            if val1 != 0:
                #currentLine += int(registers.get(cmd[2], cmd[2]))
                currentLine += int(cmd[2])
                continue
        elif cmd[0] == "out":
            out = int(registers.get(cmd[1], cmd[1]))
            #print("out:", out)
            if lastOut == 0 and out == 1:
                outCount += 1
                lastOut = 1
            elif lastOut == 1 and out == 0:
                outCount += 1
                lastOut = 0
            else:
                #print("out BAD")
                return 1
            if outCount > 20:
                return 0
        currentLine += 1
    print("finishing, outCount", registers)
    return outCount > 2 and 0 or 1

runProgram(0)

print("Done!")
