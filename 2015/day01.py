#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/1
"""
import aoc

PUZZLE = aoc.Puzzle(day=1, year=2015)


def find_floor():
    """Solve part A"""
    floor = 0
    floor += PUZZLE.input.count('(')
    floor -= PUZZLE.input.count(')')
    return floor


def find_basement():
    """Solve part B"""
    floor, position = 0, 0
    for staircase in PUZZLE.input:
        position += 1
        floor += 1 if staircase == '(' else -1
        if floor == -1:
            return position
    return None


if __name__ == "__main__":
    PUZZLE.report_a(find_floor())
    PUZZLE.report_b(find_basement())
