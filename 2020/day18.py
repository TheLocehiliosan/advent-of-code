#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/18
"""
import operator
import re
import aoc

PUZZLE = aoc.Puzzle(day=18, year=2020)

GROUP = re.compile(r'\(([^)(]+)\)')
ADD = re.compile(r'(\d+\s+\+\s+\d+)')
OPS = {'+': operator.add, '*': operator.mul}


def calc(expr, add=False):
    """Calculate an expression"""
    while grouping := GROUP.findall(expr):
        expr = GROUP.sub(calc(grouping[0], add=add), expr, 1)
    if add:
        while addition := ADD.findall(expr):
            expr = ADD.sub(calc(addition[0], add=False), expr, 1)
    terms = (x for x in expr.split())
    result = int(next(terms))
    for opr in terms:
        result = OPS[opr](result, int(next(terms)))
    return str(result)


def solve():
    """Solve puzzle"""
    sum_a, sum_b = 0, 0
    for line in PUZZLE.input.splitlines():
        sum_a += int(calc(line))
        sum_b += int(calc(line, add=True))
    PUZZLE.report_a(sum_a)
    PUZZLE.report_b(sum_b)


if __name__ == "__main__":
    solve()
