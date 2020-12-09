#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/9
"""
import itertools
import aoc

PUZZLE = aoc.Puzzle(day=9, year=2020)


def find_oddball(series):
    """Find oddball in series"""
    for idx in range(25, len(series)):
        sums = map(sum, itertools.combinations(series[idx-25:idx], 2))
        if series[idx] not in sums:
            return series[idx]
    return None


def solve():
    """Solve puzzle"""
    series = list(map(int, PUZZLE.input.splitlines()))
    oddball = find_oddball(series)
    PUZZLE.report_a(oddball)
    for idx in range(len(series)):
        for siz in range(idx + 1, len(series)):
            total = sum(series[idx:siz])
            if len(series[idx:siz]) > 1 and total == oddball:
                PUZZLE.report_b(max(series[idx:siz]) + min(series[idx:siz]))


if __name__ == "__main__":
    solve()
