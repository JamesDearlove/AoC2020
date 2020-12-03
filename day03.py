import os
import math

inputfile = "day03.txt"

def getPoint(inputdata, row, col):
    length = len(inputdata[0]) - 1
    return 1 if inputdata[row][col % length] == "#" else 0

def part1(inputdata):
    repeat = len(inputdata[0]) - 1
    
    treeHits = 0

    row = 0
    for line in inputdata:
        col = (row * 3) % repeat
        
        if (line[col] == "#"):
            treeHits += 1

        row += 1

    return treeHits

def part2(inputdata):
    repeat = len(inputdata[0]) - 1
    
    results = [0,0,0,0,0]

    row = 0
    for line in inputdata:
        results[0] += getPoint(inputdata, row, row)
        results[1] += getPoint(inputdata, row, row * 3)
        results[2] += getPoint(inputdata, row, row * 5)
        results[3] += getPoint(inputdata, row, row * 7)
        if row <= (len(inputdata) - 1) / 2:
            results[4] += getPoint(inputdata, row * 2, row)

        row += 1

    res = 1
    for i in results:
        res *= i
    
    return res

if __name__ == "__main__":
    f = open(inputfile, "r");
    data = [line for line in f.readlines()]

    print("Part 1: " + str(part1(data)))
    print("Part 2: " + str(part2(data)))
