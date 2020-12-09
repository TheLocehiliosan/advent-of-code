#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/1
"""
import functools
import itertools
import operator
import aoc

PUZZLE = aoc.Puzzle(day=1, year=2020)


def solve(count):
    """Solve puzzle"""
    dataset = map(int, PUZZLE.input.splitlines())
    for nums in itertools.combinations_with_replacement(dataset, count):
        if sum(nums) == 2020:
            return functools.reduce(operator.mul, nums)
    return None


if __name__ == "__main__":
    PUZZLE.report_a(solve(2))
    PUZZLE.report_b(solve(3))
