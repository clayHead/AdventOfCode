# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/2

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 2
    reports = []

    def prep_input(self):
        for line in self.input:
            split = line.split()

            levels = []
            for var in split:
                levels.append(int(var))

            self.reports.append(levels)

    def check_report(self, report):
        first = report[0]
        second = report[1]
        if (first > second):
            increasing = False
        elif (first < second):
            increasing = True
        else:
            return 0

        safe = True
        for i in range(1, len(report)):
            if (increasing and report[i] < report[i-1]):
                safe = False
                break
            elif (not increasing and report[i] > report[i-1]):
                safe = False
                break
            if (abs(report[i] - report[i-1])) > 3 or (abs(report[i] - report[i-1])) < 1:
                safe = False
                break
        
        if (safe is True):
            return 1
        return 0
    
    def process(self, dampenerOn=True):
        safeCount = 0

        for report in self.reports:
            safe = self.check_report(report)

            if (safe == 1):
                safeCount+=1
            elif (safe == 0 and dampenerOn):
                for i in range(len(report)):
                    dampened = report[:]
                    dampened.pop(i)
                    safe = self.check_report(dampened)
                    if (safe == 1):
                        safeCount+=1
                        break
                
        return safeCount


    # @answer(1234)
    def part_1(self) -> int:
        return self.process(False)

    # @answer(1234)
    def part_2(self) -> int:
        return self.process()

    @answer((591, 621))
    def solve(self) -> tuple[int, int]:
        self.prep_input()
        return self.part_1(), self.part_2()

        