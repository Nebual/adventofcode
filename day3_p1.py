bits_seen = [0,0,0,0,0,0,0,0,0,0,0,0]
rows = 0
with open("day3_input.txt") as f:
    for line in f:
        rows += 1
        for i in range(len(bits_seen)):
            bits_seen[i] += int(line[i])
most_bits = ""
least_bits = ""
print(bits_seen)
for i in range(len(bits_seen)):
    most_bits += bits_seen[i] > rows/2 and "1" or "0"
    least_bits += bits_seen[i] > rows/2 and "0" or "1"

most = int(most_bits, 2)
least = int(least_bits, 2)
        
print("Answer: ", most, least, most * least)
