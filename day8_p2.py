sum = 0
with open("day8_input.txt") as f:
    for line in f:
        (tenSegments, fourNumbers) = [nums.strip().split(" ") for nums in line.split(" | ")]
        lengths = [len(x) for x in tenSegments]
        oneSegments = tenSegments[lengths.index(2)]
        fourSegments = tenSegments[lengths.index(4)]
        sevenSegments = tenSegments[lengths.index(3)]
        eightSegments = tenSegments[lengths.index(7)]
        
        aaaa = list(set(sevenSegments) - set(oneSegments))[0]
        remaining = set(tenSegments) - set([oneSegments, fourSegments, sevenSegments, eightSegments])
        for segments in remaining:
            if len(set(fourSegments).intersection(segments)) == 4:
                nineSegments = segments
                break
        remaining -= set([nineSegments])

        for segments in remaining:
            if len(segments) == 6 and len(set(oneSegments).intersection(segments)) == 2:
                zeroSegments = segments
                break
        remaining -= set([zeroSegments])

        for segments in remaining:
            if len(segments) == 6:
                sixSegments = segments
                break
        remaining -= set([sixSegments])

        for segments in remaining:
            if len(set(oneSegments).intersection(segments)) == 2:
                threeSegments = segments
                break
        remaining -= set([threeSegments])

        for segments in remaining:
            if len(set(fourSegments).intersection(segments)) == 3:
                fiveSegments = segments
                break
        remaining -= set([fiveSegments])

        twoSegments = list(remaining)[0]

        orderedSegments = (
            sorted(zeroSegments),
            sorted(oneSegments),
            sorted(twoSegments),
            sorted(threeSegments),
            sorted(fourSegments),
            sorted(fiveSegments),
            sorted(sixSegments),
            sorted(sevenSegments),
            sorted(eightSegments),
            sorted(nineSegments)
        )

        theNumber = ''
        for segment in fourNumbers:
            theNumber += str(orderedSegments.index(sorted(segment)))
        sum += int(theNumber)
print("Part 2: ", sum)

