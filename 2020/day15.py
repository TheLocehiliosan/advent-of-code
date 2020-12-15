#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/15
"""
import aoc

PUZZLE = aoc.Puzzle(day=15, year=2020)


def solve(target=2020):
    """Solve puzzle"""
    start = list(map(int, PUZZLE.input.split(',')))
    seq, index = dict(), 0
    for idx, value in enumerate(start[:-1]):
        seq[value] = idx + 1
        index = idx + 1
    next_num = start[-1]
    while index < target:
        index += 1
        value = index - seq[next_num] if next_num in seq else 0
        seq[next_num] = index
        next_num = value
    return next(key for (key, val) in seq.items() if val == index)


if __name__ == "__main__":
    PUZZLE.report_a(solve(2020))
    PUZZLE.report_b(solve(30000000))
