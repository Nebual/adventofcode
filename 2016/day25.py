with open("2016/day25.txt") as f:
    instructions = [line.strip().split(" ") for line in f.readlines()]


def runProgram(startingA):
    currentLine = 0
    registers = dict()
    registers['a'] = startingA
    registers['b'] = 0
    registers['c'] = 0
    registers['d'] = 0
    lastOut = None
    outCount = 0
    #loopCount = 0

    while True: #loopCount < 100000:
        cmd = instructions[currentLine]
        # loopCount += 1
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
            if out != lastOut:
                outCount += 1
                lastOut = out
            else:
                #print("out BAD")
                return 1
            if outCount > 20:
                return 0
        currentLine += 1
    print("finishing, outCount", outCount)
    return outCount > 2 and 0 or 1

for x in range(1000):
    print("Testing ", x)
    result = runProgram(x)
    if result == 0:
        print("Answer: ", x)
        break

print("Done!")
