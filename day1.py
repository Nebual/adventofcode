previous = None
countIncreases = 0
with open("day1_input.txt", "r") as f:
    for line in f.readlines():
        amount = int(line)
        if previous is not None and previous < int(line):
            print(int(line), "is greater than previous", previous)
            countIncreases += 1
        previous = int(line)
print("Answer: ", countIncreases)
