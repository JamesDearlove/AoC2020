import os

inputfile = "day01.txt"

def part1(inputdata):
    for i in inputdata:
        for j in inputdata:
            if i + j == 2020:
                return i * j

def part2(inputdata):
    for i in inputdata:
        for j in inputdata:
            for k in inputdata:
                if i + j + k == 2020:
                    return i * j * k

if __name__ == "__main__":
    
    f = open(inputfile, "r");
    data = [int(line) for line in f.readlines()]

    print("Part 1: " + str(part1(data)))
    print("Part 2: " + str(part2(data)))
