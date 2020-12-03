import os

inputfile = "day02.txt"

def parseLine(inputdata):
    return inputdata.replace("-", " ").split(" ")

def part1(inputdata):
    validCount = 0

    for line in inputdata:
        s = parseLine(line)
        minChar = int(s[0])
        maxChar = int(s[1])
        checkChar = s[2][0]
        
        charCount = 0
        for letter in s[3]:
            if letter == checkChar:
                charCount += 1 
        
        if charCount >= minChar and charCount <= maxChar:
            validCount += 1

    return validCount

def part2(inputdata):
    validCount = 0

    for line in inputdata:
        s = parseLine(line)
        fstLoc = int(s[0]) - 1
        secLoc = int(s[1]) - 1
        checkChar = s[2][0]

        if (s[3][fstLoc] == checkChar) + (s[3][secLoc] == checkChar) == 1:
            validCount += 1

    return validCount

if __name__ == "__main__":
    f = open(inputfile, "r");
    data = [line for line in f.readlines()]

    print("Part 1: " + str(part1(data)))
    print("Part 2: " + str(part2(data)))
