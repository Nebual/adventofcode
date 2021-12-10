IS_PART2 = True
with open("2016/day23.txt") as f:
    instructions = [line.strip().split(" ") for line in f.readlines()]


def runProgram(startingA):
    global instructions
    currentLine = 0
    registers = dict()
    registers['a'] = startingA
    registers['b'] = 0
    registers['c'] = 0
    registers['d'] = 0
    lastOut = 0
    outCount = 0
    loopCount = 0

    while currentLine < len(instructions):
        cmd = instructions[currentLine]
        if cmd[0] == "cpy":
            val1 = int(registers.get(cmd[1], cmd[1]))
            val2 = cmd[2]
            if val2 in registers:
                registers[val2] = val1
        elif cmd[0] == "inc":
            registers[cmd[1]] += 1
        elif cmd[0] == "dec":
            registers[cmd[1]] -= 1
        elif cmd[0] == "jnz":
            val1 = int(registers.get(cmd[1], cmd[1]))
            if val1 != 0:
                currentLine += int(registers.get(cmd[2], cmd[2]))
                # currentLine += int(cmd[2])
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
        elif cmd[0] == "tgl":
            target = currentLine + int(registers.get(cmd[1], cmd[1]))
            if target < 0 or target >= len(instructions):
                pass
            elif len(instructions[target]) == 2:
                instructions[target][0] = instructions[target][0] == "inc" and "dec" or "inc"
            else:
                instructions[target][0] = instructions[target][0] == "jnz" and "cpy" or "jnz"
        currentLine += 1
    print("finishing, outCount", registers)

runProgram(IS_PART2 and 12 or 7)

print("Done!")
