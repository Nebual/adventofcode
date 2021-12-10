import re

previous = None
depth = 0
forward = 0

with open("day2_input.txt", "rb") as f:
    for line in f.readlines():
        result = re.search(r"(forward|down|up) (\d+)", str(line))

        direction = result[1]
        amount = int(result[2])
        if direction == "forward":
            forward += amount
        elif direction == "down":
            depth += amount
        elif direction == "up":
            depth -= amount
print("Answer: ", depth, forward, depth * forward)
