#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/12
"""
import aoc

PUZZLE = aoc.Puzzle(day=12, year=2020)
DIRECTIONS = {'E': (1, 0), 'S': (0, -1), 'W': (-1, 0), 'N': (0, 1)}


def move(heading, x, y, dist):
    """Move"""
    if isinstance(heading, tuple):
        (delta_x, delta_y) = heading
    else:
        (delta_x, delta_y) = DIRECTIONS[heading]
    x += delta_x * dist
    y += delta_y * dist
    return x, y


def adjust_heading(heading, direction, dist):
    """Change direction"""
    (x, y) = heading
    (delta_x, delta_y) = DIRECTIONS[direction]
    x += delta_x * dist
    y += delta_y * dist
    return (x, y)


def rotate_heading(heading, direction):
    """Rotate heading"""
    (x, y) = heading
    if direction == 'R':
        x, y = y, -x
    else:
        x, y = -y, x
    return (x, y)


def solve(part='a'):
    """Solve puzzle"""
    x, y = 0, 0
    heading = (1, 0) if part == 'a' else (10, 1)
    for line in PUZZLE.input.splitlines():
        instr, dist = line[0], int(line[1:])
        if instr in 'RL':
            for _ in range(dist // 90):
                heading = rotate_heading(heading, instr)
        elif instr == 'F':
            x, y = move(heading, x, y, dist)
        else:
            if part == 'a':
                x, y = move(instr, x, y, dist)
            else:
                heading = adjust_heading(heading, instr, dist)
    return abs(x) + abs(y)


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
