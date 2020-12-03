#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
https://adventofcode.com/2020/day/3
"""
import itertools
import aoc

PUZZLE = aoc.Puzzle(day=3, year=2020)


def generate(row):
    """Generate infinite terrain"""
    while True:
        for char in row:
            yield char


def count_trees(right, down):
    """Count tress matching slope"""
    col, trees = 0, 0
    rows = list(PUZZLE.input.splitlines())
    for row in rows[down::down]:
        col += right
        if list(itertools.islice(generate(row), col + 1))[-1] == '#':
            trees += 1
    return trees


def solve(slopes):
    """Solve puzzle"""
    trees = 1
    for slope in slopes:
        trees = trees * count_trees(*slope)
    return trees


if __name__ == "__main__":
    PUZZLE.report_a(solve([[3, 1]]))
    PUZZLE.report_b(solve([[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]))
