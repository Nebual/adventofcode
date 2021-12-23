binaryString = ""
with open("day16_input.txt") as f:
    hexString = f.readlines()[0].strip()
    for char in hexString:
        binaryString += bin(int(char, 16))[2:].zfill(4)

# binaryString = ""
# for char in "38006F45291200":
#     binaryString += bin(int(char, 16))[2:].zfill(4)

def doOperation(type, numbers):
    if type == 0:
        return sum(numbers)
    if type == 1:
        product = numbers[0]
        for num in numbers[1:]:
            product *= num
        return product
    if type == 2:
        return min(numbers)
    if type == 3:
        return max(numbers)
    if type == 5:
        return numbers[0] > numbers[1] and 1 or 0
    if type == 6:
        return numbers[0] < numbers[1] and 1 or 0
    if type == 7:
        return numbers[0] == numbers[1] and 1 or 0

versionsFound = []
def parsePacket(remainder):
    version = int(remainder[0:3], 2)
    versionsFound.append(version)
    typeId = int(remainder[3:6], 2)
    remainder = remainder[6:]
    if typeId == 4:
        # literal
        numberBits = ""
        while remainder[0] == "1":
            numberBits += remainder[1:5]
            remainder = remainder[5:]
        numberBits += remainder[1:5]
        remainder = remainder[5:]
        number = int(numberBits, 2)
        return remainder, number
    elif remainder[0] == "0":
        totalLength = int(remainder[1:16], 2)
        remainder = remainder[16:]
        lengthInitial = len(remainder)
        subPackets = []
        while (lengthInitial - totalLength) < len(remainder):
            remainder, number = parsePacket(remainder)
            subPackets.append(number)
        return remainder, doOperation(typeId, subPackets)
    elif remainder[0] == "1":
        numberSubPackets = int(remainder[1:12], 2)
        remainder = remainder[12:]
        subPackets = []
        for i in range(numberSubPackets):
            remainder, number = parsePacket(remainder)
            subPackets.append(number)
        return remainder, doOperation(typeId, subPackets)

remainder, number = parsePacket(binaryString)
print("Answer: ", sum(versionsFound), remainder, number)
