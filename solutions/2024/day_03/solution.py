# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/3

from ...base import StrSplitSolution, answer
import re
patern = "mul\((\d{1,3},\d{1,3})\)"


class Solution(StrSplitSolution):
    _year = 2024
    _day = 3

    # @answer(1234)
    def part_1(self) -> int:
        sum = 0

        for line in self.input:
            matches = re.findall(patern, line)

            for match in matches:
                split = match.split(',')

                var1 = int(split[0])
                var2 = int(split[1])

                sum += var1 * var2
        
        return sum

    # @answer(1234)
    def part_2(self) -> int:
        sum = 0
        instructions = []
        mulEnabled = True

        for line in self.input:
            # Parse the lines charecter by charecter
            for x in range(len(line)):
                # First check if we need to enable/disable mul
                if (line[x] == 'd'):
                    if (line[x:x+4] == 'do()'):
                        #print('enabled')
                        mulEnabled = True
                    elif (line[x:x+7] == 'don\'t()'):
                        #print('disabled')
                        mulEnabled = False
                elif (line[x] == 'm' and mulEnabled):
                    if (line[x:x+4] == 'mul('):
                        # Start after where we know the numerics are and work until the biggest possbile instruction
                        # Find the end paren and then create an instriction based off that
                        add = 5
                        for i in range(add,13):
                            print(line[x:x+add])
                            if (line[x+add] == ')'):
                                instructions.append(line[x:x+add])
                                break
                            else:
                                add += 1
        
        for instruction in instructions:
            # The above parsing includes results like mul(75), exclude these
            if ',' in instruction:
                # Strip away all chars before and after ints and ','
                instruction = instruction.replace('mul(', '')
                instruction = instruction.replace(')', '')

                print(instruction)
                split = instruction.split(',')
                var1 = int(split[0])
                var2 = int(split[1])
                
                sum += var1 * var2

        return sum

    # @answer((1234, 4567))
    def solve(self) -> tuple[int, int]:
        return self.part_1(), self.part_2()
