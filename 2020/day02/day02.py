#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
https://adventofcode.com/2020/day/2
"""
import re
import aoc

PUZZLE = aoc.Puzzle(day=2, year=2020)


def solve(part):
    """Solve puzzle"""
    valid = 0
    for line in PUZZLE.input.splitlines():
        (start, end, letter, passwd) = re.split(r'[-: ]+', line)
        if part == 'a':
            if int(start) <= passwd.count(letter) <= int(end):
                valid += 1
        else:
            letters = {passwd[int(_)-1] for _ in (start, end)}
            if len(letters) == 2 and letter in letters:
                valid += 1
    return valid


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
