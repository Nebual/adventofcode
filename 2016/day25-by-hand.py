import sys

def runProgram(a):
    b = 0
    d = 0
    lastOut = ""
    outCount = 0

    d = 282 * 9 + a
    while True:
        a = d # L9
        if outCount > 0:
            xxx = 1
        while True:
            b = a % 2
            a = (a - b) // 2
            out = str(b) # L28
            print(out, end="")
            if out == lastOut:
                return outCount
            outCount += 1
            lastOut = out
            if outCount > 1000:
                return outCount
            if a == 0: # L29
                break # goto L10


# known = [0, 1,0,3,0,1,0,2,0,1,0,5,0,1,0,2,0,1,0,3]
# for x in range(20):
#     if known[x] != runProgram(x):
#         print("TEST FAILED", x, runProgram(x))
#         sys.exit(1)

for x in range(500000):
    outCount = runProgram(x)
    print("Tested", x, ",", outCount)
    if outCount > 1000:
        print("Answer: ", x)
        break
