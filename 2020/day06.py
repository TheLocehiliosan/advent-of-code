#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/6
"""
import aoc

PUZZLE = aoc.Puzzle(day=6, year=2020)


def answers():
    """Generate groups of answers"""
    for group in PUZZLE.input.split('\n\n'):
        lines = group.splitlines()
        yield len(lines), ''.join(lines)


def solve():
    """Solve puzzle"""
    total_a, total_b = 0, 0
    for people, ans in answers():
        for letter in set(ans):
            total_a += 1
            if ans.count(letter) == people:
                total_b += 1
    PUZZLE.report_a(total_a)
    PUZZLE.report_b(total_b)


if __name__ == "__main__":
    solve()
