import re

previous = None
aim = 0
depth = 0
forward = 0

with open("day2_input.txt", "rb") as f:
    for line in f.readlines():
        result = re.search(r"(forward|down|up) (\d+)", str(line))

        direction = result[1]
        amount = float(result[2])
        if direction == "forward":
            forward += amount
            depth += amount * aim
        elif direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount
print("Answer: ", depth, forward, depth * forward)
