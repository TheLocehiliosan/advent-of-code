#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
https://adventofcode.com/2020/day/5
"""
import aoc

PUZZLE = aoc.Puzzle(day=5, year=2020)


def seat(code):
    """Convert to seat number"""
    row = int(str(code[:7]).replace('F', '0').replace('B', '1'), 2)
    col = int(str(code[7:]).replace('L', '0').replace('R', '1'), 2)
    return row * 8 + col


def solve(part):
    """Solve puzzle"""
    seats = sorted(seat(_) for _ in PUZZLE.input.splitlines())
    if part == 'a':
        return seats[-1]
    for index, value in enumerate(range(seats[0], seats[-1])):
        if seats[index] != value:
            return value
    return None


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
