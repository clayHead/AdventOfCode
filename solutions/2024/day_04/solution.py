# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/4

from ...base import StrSplitSolution, answer

class Grid:
    lines = []
    yBound = -1
    xBound = -1
    xCrossBound = -1
    yCrossBound = -1

    def __init__(self, lines):
        self.lines = lines
        self.xBound = len(self.lines)-3
        self.yBound = len(self.lines[0])-3
        self.xCrossBound = len(self.lines)-1
        self.yCrossBound = len(self.lines[0])-1

    def __str__(self):
        string = ''
        for line in self.lines:
            for i in range(len(line)):
                string += line[i]
            string += '\n'
        return string
    
    def At(self, x, y):
        return self.lines[x][y]

    def CheckUp(self, x, y):
        if x > 2:
            if self.At(x,y) + self.At(x-1,y) + self.At(x-2,y) + self.At(x-3,y) == 'XMAS':
                return True
        else: 
            return False
    
    def CheckDown(self, x, y):
        if x < self.xBound:
            if self.At(x,y) + self.At(x+1,y) + self.At(x+2,y) + self.At(x+3,y) == 'XMAS':
                return True
        else:
            return False
    
    def CheckLeft(self, x, y):
        if y > 2:
            if self.At(x,y) + self.At(x,y-1) + self.At(x,y-2) + self.At(x,y-3) == 'XMAS':
                return True
        else: 
            return False
        
    def CheckRight(self, x, y):
        if y < self.yBound:
            if self.At(x,y) + self.At(x,y+1) + self.At(x,y+2) + self.At(x,y+3) == 'XMAS':
                return True
        else:
            return False
    
    def CheckUpRight(self, x, y):
        if y < self.yBound and x > 2:
            if self.At(x,y) + self.At(x-1,y+1) + self.At(x-2,y+2) + self.At(x-3,y+3) == 'XMAS':
                return True
        else:
            return False
        
    def CheckUpLeft(self, x, y):
        if y > 2 and x > 2:
            if self.At(x,y) + self.At(x-1,y-1) + self.At(x-2,y-2) + self.At(x-3,y-3) == 'XMAS':
                return True
        else:
            return False
        
    def CheckDownRight(self, x, y):
        if x < self.xBound and y < self.yBound:
            if self.At(x,y) + self.At(x+1,y+1) + self.At(x+2,y+2) + self.At(x+3,y+3) == 'XMAS':
                return True
        else:
            return False
    
    def CheckDownLeft(self, x, y):
        if x < self.xBound and y > 2:
            if self.At(x,y) + self.At(x+1,y-1) + self.At(x+2,y-2) + self.At(x+3,y-3) == 'XMAS':
                return True
        else:
            return False
    
    def CheckAll(self, x, y):
        count = 0
        if (self.CheckUp(x,y)):
            count += 1
        if (self.CheckDown(x,y)):
            count += 1
        if (self.CheckLeft(x,y)):
            count += 1
        if (self.CheckRight(x,y)):
            count += 1
        if (self.CheckUpRight(x,y)):
            count += 1
        if (self.CheckUpLeft(x,y)):
            count += 1
        if (self.CheckDownRight(x,y)):
            count += 1
        if (self.CheckDownLeft(x,y)):
            count += 1
        return count
    
    def ScanList(self) -> tuple[int, int]:
        countPart1 = 0
        countPart2 = 0

        for x in range(len(self.lines)):
            for y in range(len(self.lines[0])-1):
                countPart1 += self.CheckAll(x, y)
                if self.CheckX(x,y):
                    countPart2 += 1
        
        return countPart1, countPart2

    def CheckX(self, x, y):
        if x > 0 and x < self.xCrossBound and y > 0 and y < self.yCrossBound:
            if self.At(x,y) == 'A':
                topLeft = self.At(x-1,y-1)
                topRight = self.At(x-1,y+1)
                bottomLeft = self.At(x+1,y-1)
                bottomRight = self.At(x+1,y+1)
                if (((topLeft == 'M' and bottomRight == 'S') or (topLeft == 'S' and bottomRight == 'M')) and
                   ((topRight == 'M' and bottomLeft == 'S') or (topRight == 'S' and bottomLeft == 'M'))):
                    return True

class Solution(StrSplitSolution):
    _year = 2024
    _day = 4

    # @answer(1234)
    def part_1(self) -> int:
        pass

    # @answer(1234)
    def part_2(self) -> int:
        pass

    @answer((2662, 2034))
    def solve(self) -> tuple[int, int]:
        print(self.input)
        grid = Grid(self.input)
        return grid.ScanList()
