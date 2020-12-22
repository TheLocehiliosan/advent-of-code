#!/usr/bin/env python3
"""
https://adventofcode.com/YEAR/day/DAY
"""
import aoc

PUZZLE = aoc.Puzzle(day=DAY, year=YEAR)


def solve():
    """Solve puzzle"""
    print(PUZZLE.input)
    PUZZLE.report_a(None)
    PUZZLE.report_b(None)


if __name__ == "__main__":
    solve()
