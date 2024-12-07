# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/6

from ...base import StrSplitSolution, answer
import time

class Guard:
    positionX = -1
    positionY = -1
    direction = '^'

    def __init__(self, x, y, direction='^'):
        self.positionX = x
        self.positionY = y
        self.direction = direction
    
    def move(self, turn=False):
        if turn:
            if self.direction == '^':
                self.direction = '>'
            elif self.direction == '>':
                self.direction = 'v'
            elif self.direction == 'v':
                self.direction = '<'
            else:
                self.direction = '^'

        if self.direction == '^':
            # Move Up
            self.positionY = self.positionY - 1
        elif self.direction == '>':
            # Move Right
            self.positionX = self.positionX + 1
        elif self.direction == 'v':
            # Move Down
            self.positionY = self.positionY + 1
        else:
            # Move Right
            self.positionX = self.positionX - 1

    def get_next(self, turn=False) -> tuple[int,int]:
        direction = self.direction
        if turn:
            if self.direction == '^':
                direction = '>'
            elif self.direction == '>':
                direction = 'v'
            elif self.direction == 'v':
                direction = '<'
            else:
                direction = '^'

        if direction == '^':
            return self.positionX, self.positionY - 1
        elif direction == '>':
            return self.positionX + 1, self.positionY
        elif direction == 'v':
            return self.positionX, self.positionY + 1
        else:
            return self.positionX - 1, self.positionY

class Grid:
    guard = None
    lines = []
    loops = 0

    startingX = None
    startingY = None
    startingDirection = '^'

    def __init__(self, lines):
        foo = []
        visitX = None
        visitY = None
        for y, line in enumerate(lines):
            #print(f'{line} : {list(line)}')
            for x, char in enumerate(line):
                # Initial is always up
                if char == '^':
                    # Set up guard and visit first position
                    self.guard = Guard(x, y, char)
                    self.startingX = x
                    self.startingY = y
                    #print(f'{x} {y}')
                    visitX = x
                    visitY = y
            foo.append(list(line))
        self.lines = foo
        self.visit(visitX, visitY)

    def print(self) -> str:
        for line in self.lines:
            join = ''.join(line)
            print(join)

    def at(self, x, y):
        return self.lines[y][x]
    
    def visit(self, x, y):
        self.lines[y][x] = 'X'

    def make_obstruction(self, x, y):
        self.lines[y][x] = '#'

    def detect_loop(self) -> bool:
        # This is Incorrect
        if (self.guard.positionX == self.startingX and 
            self.guard.positionY == self.startingY and 
            self.guard.direction == self.startingDirection):
            return True
    
    # True if guard still on map
    def check_bound(self, nextPos: tuple[int,int]) -> bool:
        # This is so we can check future postions (arguments not null)
        if nextPos is None:
            trueX = self.guard.positionX
            trueY = self.guard.positionY
        else:
            trueX = nextPos[0]
            trueY = nextPos[1]  

        # Check right/left
        if trueX < 0 or trueX > len(self.lines)-1:
            return False
        # Check up/down
        if trueY < 0 or trueY > len(self.lines[0])-1:
            return False
        return True
    
    def should_turn(self) -> bool:
        currentX = self.guard.positionX
        currentY = self.guard.positionY

        if self.guard.direction == '^':
            if self.check_bound((currentX, currentY-1)) and self.at(currentX, currentY-1) == '#':
                # We are turning
                return True
        elif self.guard.direction == '>':
            if self.check_bound((currentX+1, currentY)) and self.at(currentX+1, currentY) == '#':
                # We are turning
                return True
        elif self.guard.direction == 'v':
            if self.check_bound((currentX, currentY+1)) and self.at(currentX, currentY+1) == '#':
                # We are turning
                return True
        elif self.guard.direction == '<':
            if self.check_bound((currentX-1, currentY)) and self.at(currentX-1, currentY) == '#':
                # We are turning
                return True
        return False
    
    # True if we can move to the next position, True if next move is turn
    def check_next(self) -> tuple[bool,bool]:
        turn = self.should_turn()
        nextPos = self.guard.get_next(turn)
        #print(f'\nNext move ({self.guard.positionX,self.guard.positionY} -> {nextPos}) is in bound: {self.check_bound(nextPos)}')
        return self.check_bound(nextPos), turn

    # Moves the guard and marks the new position as visited
    def move(self, turn):
        self.guard.move(turn)
        #print(f'New Pos: {self.guard.positionX,self.guard.positionY}')
        self.visit(self.guard.positionX, self.guard.positionY)

    # Does one complete time step by:
    #   Checking the next move
    #       If next move is in bound, move, return true to continue
    #       if next move is out of bound, return false to quit
    # Returns True if can continue, returns True if loop is detected
    def time_step(self, int) -> tuple[bool,bool]:
        #print(f'step: {int} {self.guard.direction} {self.should_turn()} {self.guard.positionX} {self.guard.positionY}')
        nextStep = self.check_next()
        if nextStep[0]:
            self.move(nextStep[1])
            return True, self.detect_loop()
        else:
            # If going out of bounds there can't be a loop
            return False, None
        
    def get_visited(self) -> int:
        count = 0
        for x, line in enumerate(self.lines):
            count += line.count('X')
        return count

class Solution(StrSplitSolution):
    _year = 2024
    _day = 6

    # Returns a num if loop is detected
    def loop(self, grid, max) -> int:
        stepNum = 0
        continueFlag = True
        while (continueFlag):
            stepNum += 1
            if stepNum >= max:
                break
            #grid.print()
            result = grid.time_step(stepNum)
            continueFlag = result[0]
            if result[1]:
                return 1
            elif not continueFlag:
                return 0

    def iterate(self, grid, count):
        stepNum = 0
        for i in range(count):
            stepNum += 1
            grid.time_step(stepNum)

    @answer(5199)
    def part_1(self) -> int:
        grid = Grid(self.input)
        self.loop(grid, 10000)
        return grid.get_visited()

    # @answer(1234)
    def part_2(self) -> int:
        tic = time.perf_counter()
        iterations = 0
        skips = 0
        loops = 0
        originalGrid = Grid(self.input)
        self.loop(originalGrid, 10000)

        for y, line in enumerate(originalGrid.lines):
            for x, char in enumerate(line):
                skip = True
                if originalGrid.at(x,y) == 'X':
                    skip = False
                iterations+=1
                print(f'Iteration: {iterations} - skipping: {skip}')
                if not skip:
                    grid = Grid(self.input)
                    grid.make_obstruction(x,y)
                    #grid.print()
                    ret = self.loop(grid, 100000)
                    if ret is not None:
                        loops += 1
                else:
                    skips += 1
        toc = time.perf_counter()
        print(f'Done! Time: {toc - tic:0.4f} - Skips: {skips} - Brute Forced: {iterations-skips}')
        return loops

    # @answer((1234, 4567))
    def solve(self) -> tuple[int, int]:
        return self.part_1(), self.part_2()
