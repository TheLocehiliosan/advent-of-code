#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/15
"""
import aoc

PUZZLE = aoc.Puzzle(day=15, year=2020)


def solve():
    """Solve puzzle"""
    goal_a, goal_b = 2020, 30000000
    start = list(map(int, PUZZLE.input.split(',')))
    seq, index = dict(), 0
    for idx, value in enumerate(start[:-1]):
        seq[value] = idx + 1
        index = idx + 1
    next_num = start[-1]
    while index < goal_b:
        index += 1
        value = index - seq[next_num] if next_num in seq else 0
        seq[next_num] = index
        if index == goal_a:
            PUZZLE.report_a(next_num)
        if index == goal_b:
            PUZZLE.report_b(next_num)
        next_num = value


if __name__ == "__main__":
    solve()
