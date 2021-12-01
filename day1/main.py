## Advent of Code
## Fabian Falco
## Day 1 - Sonar Sweep
## https://adventofcode.com/2021/day/1

# function that reads file and saves into array
def readFile(fileName):
    fileObj = open(fileName, "r")
    output = fileObj.read().splitlines()
    fileObj.close()
    return output

# First Star
def largerMeasurement():
    # Use a breakpoint in the code line below to debug your script.
    measures = readFile('input')

    count = 0
    previous = 0

    for measure in measures:
        if previous != 0 and int(measure) > previous:
            count += 1
        previous = int(measure)

    print(count)
    return count

# Second Star
def largerSum():
    # Use a breakpoint in the code line below to debug your script.
    measures = readFile('input')
    count = 0
    previousSum = 0
    i = 0

    # as long as 3 measures exist
    while i+2 < len(measures):
        sum = int(measures[i]) + int(measures[i+1]) + int(measures[i+2])
        # compare previous with current sum
        if sum > previousSum and previousSum != 0:
            count += 1

        # update previous sum
        previousSum = sum
        i += 1

    print(count)
    return count

if __name__ == '__main__':
    largerMeasurement()
    largerSum()

