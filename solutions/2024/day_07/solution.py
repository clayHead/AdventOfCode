# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/7

from ...base import StrSplitSolution, answer
import time

# https://www.geeksforgeeks.org/python-merge-two-lists-alternatively/
def countList(lst1, lst2):
    zipped = [item for pair in zip(lst1, lst2 + [0])
                                 for item in pair]
    return zipped[:-1]

class Solution(StrSplitSolution):
    _year = 2024
    _day = 7

    def process_input(self) -> tuple[int,list[int]]:
        ret = []
        for line in self.input:
            split = line.split(' ')
            result1 = int(split[0][:-1])
            result2 = list(map(int, split[1:]))
            ret.append((result1,result2))
        return ret
    
    def generate_operators(self, numOperators, part2: bool) -> list[list[str]]:
        if numOperators == 1:
            if part2:
                return ('+','*', '|')
            else:
                return ('+','*')
        else:
            ret = self.generate_operators(numOperators-1, part2)
            answers = []
            for i in ret:
                answers.append('+'+i)
                answers.append('*'+i)
                if part2:
                    answers.append('|'+i)
            return answers
        
    def process_equation(self, equation) -> int:
        total = equation[0]
        for x, entry in enumerate(equation):
            if entry == '*':
                total = total*equation[x+1]
            elif entry == '+':
                total = total+equation[x+1]
            elif entry == '|':
                total = int(str(total)+str(equation[x+1]))
        return total
    
    def process(self, part2):
        lines = self.process_input()
        total = 0
        processed = set()
        allCombinations = {}
        for line in lines:
            numbers = line[1]
            numOperators = len(numbers)-1
            if numOperators not in processed:
                combitions = self.generate_operators(numOperators, part2)
                allCombinations[numOperators] = combitions
                processed.add(numOperators)

        for line in lines:
            # For each line in the input, try all left to right combinations of operators
            # Return true if any equal the desired value
            desiredValue = line[0]
            numbers = line[1]
            numOperators = len(numbers)-1

            # There are a number of possible combinations equal to 2^numOperators
            # We can recursively generate all possible combitions of operators
            #   then try each one
            for combition in allCombinations[numOperators]:
                equation  = countList(numbers, list(combition))
                if self.process_equation(equation) == desiredValue:
                    total+=desiredValue
                    # We only want to count this line once
                    break
        return total
        
    @answer(2299996598890)
    def part_1(self) -> int:
        return self.process(False)
            
    @answer(362646859298554)
    def part_2(self) -> int:
        return self.process(True)

    # @answer((1234, 4567))
    def solve(self) -> tuple[int, int]:
        return self.part_1(), self.part_2()
