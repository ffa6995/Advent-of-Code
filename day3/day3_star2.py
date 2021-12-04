## Advent of Code
## Fabian Falco
## Day 3 - Binary Diagnostic!
## https://adventofcode.com/2021/day/3

class DiagnosticReport:
    def __init__(self):
        self.gamma_rates = ""
        self.epsilon_rates = ""
        self.power_consumption = 0
        self.oxygen_generator_rtg = 0
        self.co2_scrubber_rtg = 0
        self.life_support_rtg = 0

    def getMostCommonBit(self, byte):
        count_bit_set = 0
        count_bit_unset = 0
        for bit in byte:
            if bit == '1':
                count_bit_set += 1
            else:
                count_bit_unset += 1
        if count_bit_set >= count_bit_unset:
            return '1'
        else:
            return '0'

    def calculatePowerConsumption(self):
        bits, bytes = readFile('input3')
        for i in range(0, 12):
            self.gamma_rates += self.getMostCommonBit(bits[i])
            if self.gamma_rates[i] == '1':
                self.epsilon_rates += '0'
            else:
                self.epsilon_rates += '1'
        self.power_consumption = int(self.gamma_rates, 2) * int(self.epsilon_rates, 2)
        return self.power_consumption

    def calculateLifeSupportRating(self):
        bits, bytes = readFile('input3')
        oxygen_bytes = bytes
        oxygen_bits = bits
        co2_bytes = bytes
        co2_bits = bits

        for i in range(0, 12):
            mostCommonBit = self.getMostCommonBit(oxygen_bits[i])
            oxygen_bytes = self.filterOnBit(oxygen_bytes, i, mostCommonBit)
            oxygen_bits = self.getNewBits(oxygen_bytes)

        for i in range(0, 12):
            mostCommonBit = self.getMostCommonBit(co2_bits[i])
            if mostCommonBit == '1':
                leastCommonBit = '0'
            else:
                leastCommonBit = '1'

            co2_bytes = self.filterOnBit(co2_bytes, i, leastCommonBit)
            co2_bits = self.getNewBits(co2_bytes)
            if len(co2_bytes) == 1:
                break
        self.life_support_rtg = int(co2_bytes[0][0], 2) * int(oxygen_bytes[0][0], 2)
        print(self.life_support_rtg)

        return self.life_support_rtg

    def filterOnBit(self, bytes, index, bit):
        new_bytes = [byte for byte in bytes if byte[0][index] == bit]
        return new_bytes

    def getNewBits(self, bytes):
        outputBits = []
        for i in range(0, 12):
            new = []
            outputBits.append(new)

        for byte in bytes:
            index = 0
            for bit in byte[0]:
                outputBits[index].append(bit)
                index += 1
        return outputBits



def readFile(fileName):
    outputBits = []
    outputBytes = []
    for i in range(0, 12):
        new = []
        outputBits.append(new)
    with open(fileName) as file:
        for line in file:

            # line_output.append(line.split())
            byte = line.split()
            outputBytes.append(byte)
            index = 0
            for bit in byte[0]:
                outputBits[index].append(bit)
                index += 1
    return outputBits, outputBytes


if __name__ == '__main__':
    diagnostic = DiagnosticReport()
    diagnostic.calculateLifeSupportRating()
