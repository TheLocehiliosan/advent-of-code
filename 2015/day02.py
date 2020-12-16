#!/usr/bin/env python3
"""
https://adventofcode.com/2015/day/2
"""
import functools
import itertools
import operator
import aoc

PUZZLE = aoc.Puzzle(day=2, year=2015)


def paper():
    """Solve part A"""
    total = 0
    for size in PUZZLE.input.splitlines():
        sides = [x * y for x, y
                 in itertools.combinations(map(int, size.split('x')), 2)]
        total += sum(sides) * 2
        total += sorted(sides)[0]
    return total


def ribbon():
    """Solve part B"""
    total = 0
    for size in PUZZLE.input.splitlines():
        edges = sorted(map(int, (size.split('x'))))
        total += sum(edges[:2]) * 2
        total += functools.reduce(operator.mul, edges)
    return total


if __name__ == "__main__":
    PUZZLE.report_a(paper())
    PUZZLE.report_b(ribbon())
