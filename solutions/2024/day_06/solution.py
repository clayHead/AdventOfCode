# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/6

from ...base import StrSplitSolution, answer
import time

from collections.abc import Iterable
from typing import TypeAlias

Vector: TypeAlias = tuple[int, int]

def vector_swap(original: Vector) -> Vector:
    return (original[1], -original[0])

def vector_add(a, b) -> Vector:
    return (a[0]+b[0], a[1]+b[1])

def guard_vector(Vector):
    if (Vector == (-1,0)):
        return '^'
    elif (Vector == (1,0)):
        return 'v'
    elif (Vector == (0,-1)):
        return '<'
    else:
        return '>'

class Guard:
    position = (-1,-1)
    direction = (-1,0)

    def __init__(self, x, y):
        self.position = (x,y)

    def __str__(self):
        if (self.direction == (-1,0)):
            return '^'
        elif (self.direction == (1,0)):
            return 'v'
        elif (self.direction == (0,-1)):
            return '<'
        else:
            return '>'

    def get_description(self):
        return f'At {self.position} facing {self.direction}'
    
    def turn(self):
        original = self.direction
        self.direction = vector_swap(original)
    
    def move(self, grid):
        while (grid[vector_add(self.position, self.direction)] == '#'):
            self.turn()
        self.position = vector_add(self.position, self.direction)

    def get_next(self, grid: dict) -> tuple[Vector,Vector]:
        direction = self.direction
        while (vector_add(self.position, direction) in grid and grid[vector_add(self.position, direction)] == '#'):
            direction = vector_swap(direction)
        return vector_add(self.position, direction), direction

class Grid:
    size = -1
    guard = None
    lines = {}
    # For each tile on the guard's path, we will store its location and
    # the direction the guard is facing
    path: list[tuple[Vector, Vector]] = []
    # NOTE Although we want to return the path in order, using a set
    # speeds up the process of checking for loops.
    path_set: set[tuple[Vector, Vector]] = set()
    path_pos: list[Vector] = []

    def __init__(self, lines):
        self.size = len(lines)
        for x in range(self.size):
            for y in range(self.size):
                self.lines[(x,y)] = lines[x][y]
                if lines[x][y] == '^':
                    self.guard = Guard(x,y)
                    self.lines[(x,y)] = '.'

    def reset(self, lines):
        #Reset to default
        self.size = -1
        self.guard = None
        self.lines = {}
        self.path: list[tuple[Vector, Vector]] = []
        self.path_set: set[tuple[Vector, Vector]] = set()
        self.path_pos: list[Vector] = []

        # Start Reset
        self.size = len(lines)
        for x in range(self.size):
            for y in range(self.size):
                self.lines[(x,y)] = lines[x][y]
                if lines[x][y] == '^':
                    self.guard = Guard(x,y)
                    self.lines[(x,y)] = '.'

    def __str__(self):
        str = ''
        for x in range(self.size):
            line = ''
            for y in range(self.size):
                if (x,y) in self.path_pos:
                    line += 'X'
                elif self.guard.position == (x,y):
                    line += self.guard.__str__()
                else:
                    line += self.lines[(x,y)]
            str+=f'{line}\n'
        return str
    
    def visit(self, path_item):
        self.path.append(path_item)
        self.path_set.add(path_item)
        self.path_pos.append(path_item[0])

    def make_obstruction(self,pos):
        self.lines[pos[0],pos[1]] = '#'

    # True if we have visited this position from this direction
    def detect_loop(self) -> bool:
        return (self.guard.position,self.guard.direction) in self.path_set
    
    # True if guard still on map
    def check_bound(self, nextPos) -> bool:
        return nextPos in self.lines
    
    # True if we can move to the next position.
    # True if we should turn
    def can_move(self) -> bool:
        nextPos, _ = self.guard.get_next(self.lines)
        return self.check_bound(nextPos)

    # Moves the guard and marks the new position as visited
    def move(self):
        self.visit((self.guard.position, self.guard.direction))
        self.guard.move(self.lines)

    # Does the entire walking sequence up to a limit to prevent infinte loops
    # Returns if we exited as a loop (counts reaching max iterations as loop)
    def walk_guard(self, maxIterations) -> bool:
        iterations = 0
        while True:
            iterations += 1
            
            if self.detect_loop() or iterations >= maxIterations:
                # If we have visited this postion from this direction, we looped
                # Or failcase break out
                #print('Loop detected')
                return True
            
            ret = self.can_move()

            # If we can't move forward
            if not ret:
                # If we reach the edge we haven't looped
                #print('Edge Reached')
                self.visit((self.guard.position,self.guard.direction))
                return False
            else:
                # Otherwise continue
                #print('Continue')
                self.move()
        
    def get_visited(self) -> int:
        return len(set(pos for pos, _ in self.path))

class Solution(StrSplitSolution):
    _year = 2024
    _day = 6

    def get_start(self):
        return Grid(self.input)

    @answer(5199)
    def part_1(self) -> int:
        grid = Grid(self.input)
        grid.walk_guard(10000)
        ret = grid.get_visited()
        print(grid)
        grid.reset(self.input)
        return ret

    # @answer(1234)
    def part_2(self) -> int:
        loops = 0
        originalGrid = Grid(self.input)
        originalGuardPostion = originalGrid.guard
        originalGrid.walk_guard(10000)
        path = originalGrid.path
        unique = originalGrid.get_visited()
        originalGrid.reset(self.input)

        # Debug variables
        skips = 0
        iterations = 0

        triedObstacles = set(Vector)
        for pathItem in path:
            iterations+=1
            print(f'Iteration: {iterations}/{len(path)}')
            grid = Grid(self.input)
            grid.reset(self.input)
            if pathItem[0] == originalGuardPostion.position and pathItem[1] == originalGuardPostion.direction:
                print(f'cant here - start: {pathItem[0]}')
                skips += 1
                continue
            elif pathItem[0] in triedObstacles:
                print(f'cant here - tried: {pathItem[0]}')
                skips += 1
                continue
            triedObstacles.add(pathItem[0])
            grid.make_obstruction(pathItem[0])
            if grid.walk_guard(10000):
                for pathItem in grid.path:
                    if pathItem[0] == originalGuardPostion.position:
                        grid.lines[pathItem[0]] = '^'
                    else:
                        grid.lines[pathItem[0]] = 'X'
                loops += 1

        print(f'SkipsActual={skips} : SkipsExpected={len(path)-unique}')
        return loops

    # @answer((1234, 4567))
    def solve(self) -> tuple[int, int]:
        return self.part_1(), self.part_2()
