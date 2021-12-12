## Advent of Code
## Fabian Falco
## Day 11 - Dumbo Octopus!
## https://adventofcode.com/2021/day/11

def runEnergy(energy_levels, times):
    flashes = 0
    new_energy_levels = energy_levels

    for k in range(times):
        print(energy_levels)
        flashed_octopussies = []
        already_flashed = []
        for i in range(10):
            for j in range(10):
                new_energy_levels[i][j] += 1
                if new_energy_levels[i][j] == 9 and (i, j) not in already_flashed:
                    already_flashed.append((i,j))
                    flashed_octopussies.append((i, j))
                    flashes += 1
                    new_energy_levels[i][j] = 0

        while len(flashed_octopussies) > 0:
            allAdjacents = []
            for flashed in flashed_octopussies:
                adjacents = getAdjacents((flashed[0], flashed[1]))
                allAdjacents += adjacents
            flashed_octopussies = []
            for adjacent in allAdjacents:
                if (adjacent[0], adjacent[1]) not in already_flashed:
                    new_energy_levels[adjacent[0]][adjacent[1]] += 1
                if new_energy_levels[adjacent[0]][adjacent[1]] == 9 \
                        and (adjacent[0], adjacent[1]) not in already_flashed:
                    already_flashed.append((adjacent[0], adjacent[1]))
                    flashed_octopussies.append((adjacent[0], adjacent[1]))
                    flashes += 1
                    new_energy_levels[adjacent[0]][adjacent[1]] = 0
        print("after step")
        print(energy_levels)
        print(flashes)
    print(flashes)



def readFile(fileName):
    output = []
    with open(fileName) as file:
        for line in file:
            l = list(line.strip())
            l2 = list(map(int, l))
            output.append(l2)
    return output


def getAdjacents(index):
    adjacents = []
    curr_row = index[0]
    curr_col = index[1]

    if curr_col > 0:
        prev_col = curr_col - 1
        adjacents.append((curr_row, prev_col))
    if curr_col < 9:
        next_col = curr_col + 1
        adjacents.append((curr_row, next_col))

    if curr_row > 0:
        prev_row = curr_row - 1
        if curr_col > 0:
            adjacents.append((prev_row, prev_col))
        adjacents.append((prev_row, curr_col))
        if curr_col < 9:
            adjacents.append((prev_row, next_col))

    if curr_row < 9:
        next_row = curr_row + 1
        if curr_col > 0:
            adjacents.append((next_row, prev_col))
        adjacents.append((next_row, curr_col))
        if curr_col < 9:
            adjacents.append((next_row, next_col))

    #print(adjacents)
    return adjacents


if __name__ == '__main__':
    energy_levels = readFile('input11')
    runEnergy(energy_levels, 100)
