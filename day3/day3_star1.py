## Advent of Code
## Fabian Falco
## Day 3 - Binary Diagnostic!
## https://adventofcode.com/2021/day/3

class DiagnosticReport:
    def __init__(self):
        self.gamma_rates = ""
        self.epsilon_rates = ""
        self.power_consumption = 0

    def getMostCommonBit(self, byte):
        count_bit_set = 0
        count_bit_unset = 0
        for bit in byte:
            if bit == '1':
                count_bit_set += 1
            else:
                count_bit_unset += 1
        if count_bit_set > count_bit_unset:
            return '1'
        else:
            return '0'

    def calculatePowerConsumption(self):
        bytes = readFile('input3')
        for i in range(0, 12):
            self.gamma_rates += self.getMostCommonBit(bytes[i])
            if self.gamma_rates[i] == '1':
                self.epsilon_rates += '0'
            else:
                self.epsilon_rates += '1'
        self.power_consumption = int(self.gamma_rates, 2) * int(self.epsilon_rates, 2)
        return self.power_consumption

def readFile(fileName):
    output = []
    for i in range(0, 12):
        new = []
        output.append(new)
    with open(fileName) as file:
        for line in file:

            # line_output.append(line.split())
            byte = line.split()
            index = 0
            for bit in byte[0]:
                output[index].append(bit)
                index += 1
    return output


if __name__ == '__main__':
    diagnostic = DiagnosticReport()
    power_consumption = diagnostic.calculatePowerConsumption()
    print(power_consumption)
