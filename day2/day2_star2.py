## Advent of Code
## Fabian Falco
## Day 2 - Dive!
## https://adventofcode.com/2021/day/2

class Submarine:
    def __init__(self, hrzPos, depth, aim):
        self.hrzPos = hrzPos
        self.depth = depth
        self.aim = aim

    def changeHrzPos(self, value):
        self.hrzPos += value
        self.depth += self.aim * value

    def changeDepth(self, value):
        self.aim += value

    def getFinalPos(self):
        return self.depth * self.hrzPos


# read file and saves each line separately in array
def readFile(fileName):
    output = []
    with open(fileName) as file:
        for line in file:
            output.append(line.split())
    return output


def processCommands(sub, commands):
    for command in commands:
        action = command[0]
        value = int(command[1])
        if action == 'forward':
            sub.changeHrzPos(value)
        elif action == 'down':
            sub.changeDepth(value)
        else:
            sub.changeDepth(-value)

if __name__ == '__main__':
    ## Star 1
    submarine = Submarine(0, 0, 0)
    commands = readFile('input2')
    processCommands(submarine, commands)
    finalPos = submarine.getFinalPos()
    print(finalPos)
