bits_seen = [0,0,0,0,0,0,0,0,0,0,0,0]

bits = []
with open("day3_input.txt", "r") as f:
    for line in f.readlines():
        bits.append(line.strip())

def findIt(bits, looking_for="most", depth=0):
    if len(bits) == 1:
        return bits
    zero_lines = []
    one_lines = []
    for line in bits:
        if line[depth] == "0":
            zero_lines.append(line)
        else:
            one_lines.append(line)
    if len(one_lines) < len(zero_lines):
        return findIt(looking_for=="most" and zero_lines or one_lines, looking_for, depth+1)
    else:
        return findIt(looking_for=="most" and one_lines or zero_lines, looking_for, depth+1)

oxygen = findIt(bits, "most")
co2 = findIt(bits, "least")

most = int(oxygen[0], 2)
least = int(co2[0], 2)
        
print("Answer: ", most, least, most * least)
