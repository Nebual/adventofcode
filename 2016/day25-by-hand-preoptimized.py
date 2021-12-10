import sys

def runProgram(a):
    b = 0
    c = 0
    d = 0
    lastOut = ""
    outCount = 0


    #d = a
    c = 9
    while True:
        b = 282
        while True:
            d += 1
            b -= 1
            if b == 0: # L6
                break
        c -= 1 # L7
        if c == 0: # L8
            break
    while True:
        a = d # L9
        while True:
            b = a # L11
            a = 0
            L21Continue = True
            while L21Continue:
                c = 2 # L13
                while True:
                    if b == 0: # L14
                        L21Continue = False #goto L21
                        break
                    else:
                        b -= 1 # L16
                        c -= 1 # L17
                        if c == 0: break # L18
                if L21Continue:
                    a += 1 # L19
                # L20
            b = 2 # L21
            while True:
                if c == 0: # L22, L23
                    break # goto L27
                b -= 1 # L24
                c -= 1 # L25
                # L26
            # L27
            out = str(b) # L28
            #print("Out: ", out)
            if out == lastOut:
                return outCount
            outCount += 1
            lastOut = out
            if outCount > 1000:
                return outCount
            if a == 0: # L29
                break # goto L10

known = [0,1,0,3,0,1,0,2,0,1,0,5,0,1,0,2,0,1,0,3]
for x in range(20):
    if known[x] != runProgram(x):
        print("TEST FAILED", x, runProgram(x))
        sys.exit(1)

for x in range(400_000, 100_000_000):
    if x % 1000 == 0: print("Testing ", x)
    outCount = runProgram(x)
    print("Tested", x, ",", outCount)
    if outCount > 1000:
        print("Answer: ", x)
        break
