## Advent of Code
## Fabian Falco
## Day 2 - Dive!
## https://adventofcode.com/2021/day/2


class Submarine:
    def __init__(self, hrztPos, depth):
        self.hrztPos = 0
        self.depth = 0

        # function to change horizontal pos
        def changeHrztPos(value):
            self.hrztPos += value

        # function to change depth
        def changeDepth(value):
            self.depth += value

        def getFinalPos():
            return self.hrztPos * self.depth


# function that reads file and saves into array
def readFile2(fileName):
    fileObj = open(fileName, "r")
    output = fileObj.readline()
    print(output)
    fileObj.close()
    return output

if __name__ == '__main__':
    sub = Submarine(0, 0)
    readFile2('input2')

