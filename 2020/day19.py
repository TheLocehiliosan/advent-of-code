#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/19
"""
import aoc
from lark import Lark, LarkError

PUZZLE = aoc.Puzzle(day=19, year=2020)


def solve(part='a'):
    """Solve puzzle"""
    rules, lines = PUZZLE.input.split('\n\n')
    if part == 'b':
        rules = rules.replace('8: 42', '8: 42 | 42 8')
        rules = rules.replace('11: 42 31', '11: 42 31 | 42 11 31')
    rules = rules.translate(str.maketrans('0123456789', 'abcdefghij'))
    parser = Lark(rules, start='a')

    total = 0
    for line in lines.splitlines():
        try:
            parser.parse(line)
            total += 1
        except LarkError:
            pass
    return total


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
