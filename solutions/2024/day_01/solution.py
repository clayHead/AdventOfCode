# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/1

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 1
    list1 = []
    list2 = []

    def prep_input(self):
        for line in self.input:
            split = line.split()

            self.list1.append(int(split[0]))
            self.list2.append(int(split[1]))

        self.list1.sort()
        self.list2.sort()

    def get_distance(self):
        distance = 0

        for x in range(len(self.list1)):
            distance += abs(self.list1[x] - self.list2[x])

        return distance

    def get_similarity(self):
        similarity = 0

        for left in self.list1:
            numRepeats = 0

            for right in self.list2:
                if left == right:
                    numRepeats += 1
            
            similarity += left * numRepeats

        return similarity

    # @answer(1234)
    def part_1(self) -> int:
        return self.get_distance()

    # @answer(1234)
    def part_2(self) -> int:
        return self.get_similarity()

    @answer((3714264, 18805872))
    def solve(self) -> tuple[int, int]:
        self.prep_input()
        return self.part_1(), self.part_2()