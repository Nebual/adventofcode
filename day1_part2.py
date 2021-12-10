previous = None
countIncreases = 0
data = []
with open("day1_input.txt", "rb") as f:
    for line in f.readlines():
        data.append(int(line))
for (i, _) in enumerate(data):
    try:
        window = data[i] + data[i+1] + data[i+2]
        if previous is not None and previous < window:
            print(window, "is greater than previous", previous)
            countIncreases += 1
        previous = window
    except IndexError:
        break
print("Answer: ", countIncreases)
