#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/10
"""
import collections
import aoc

PUZZLE = aoc.Puzzle(day=10, year=2020)


def solve():
    """Solve puzzle"""
    adps = sorted(map(int, PUZZLE.input.splitlines()))
    adps.append(adps[-1]+3)
    paths = collections.defaultdict(int, {0: 1})
    prev, ones, threes = 0, 0, 0
    for adp in adps:
        for valid_jump in range(1, 4):
            paths[adp] += paths[adp - valid_jump]
        if adp - prev == 1:
            ones += 1
        elif adp - prev == 3:
            threes += 1
        prev = adp
    PUZZLE.report_a(ones * threes)
    PUZZLE.report_b(paths[adps[-1]])


if __name__ == "__main__":
    solve()
