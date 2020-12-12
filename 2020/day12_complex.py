#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/12
"""
import aoc

PUZZLE = aoc.Puzzle(day=12, year=2020)
DIRECTIONS = {'E': 1, 'S': -1j, 'W': -1, 'N': 1j}


def move(heading, pos, dist):
    """Move"""
    if isinstance(heading, complex):
        delta = heading
    else:
        delta = DIRECTIONS[heading]
    pos += delta * dist
    return pos


def adjust_heading(heading, direction, dist):
    """Change direction"""
    delta = DIRECTIONS[direction]
    heading += delta * dist
    return heading


def rotate_heading(heading, direction):
    """Rotate heading"""
    if direction == 'R':
        return heading / 1j
    return heading * 1j


def solve(part='a'):
    """Solve puzzle"""
    pos = 0j
    heading = 1 if part == 'a' else 10+1j
    for line in PUZZLE.input.splitlines():
        instr, dist = line[0], int(line[1:])
        if instr in 'RL':
            for _ in range(dist // 90):
                heading = rotate_heading(heading, instr)
        elif instr == 'F':
            pos = move(heading, pos, dist)
        else:
            if part == 'a':
                pos = move(instr, pos, dist)
            else:
                heading = adjust_heading(heading, instr, dist)
    return abs(int(pos.real)) + abs(int(pos.imag))


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
