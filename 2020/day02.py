#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
https://adventofcode.com/2020/day/2
"""
import re
import aoc

PUZZLE = aoc.Puzzle(day=2, year=2020)


def solve():
    """Solve puzzle"""
    valid_a, valid_b = 0, 0
    for line in PUZZLE.input.splitlines():
        (start, end, letter, passwd) = re.split(r'[-: ]+', line)
        if int(start) <= passwd.count(letter) <= int(end):
            valid_a += 1
        letters = {passwd[int(_)-1] for _ in (start, end)}
        if len(letters) == 2 and letter in letters:
            valid_b += 1
    PUZZLE.report_a(valid_a)
    PUZZLE.report_b(valid_b)


if __name__ == "__main__":
    solve()
