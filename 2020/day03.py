#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
https://adventofcode.com/2020/day/3
"""
import aoc

PUZZLE = aoc.Puzzle(day=3, year=2020)


def count_trees(*slopes):
    """Count tress matching slope"""
    answer = 1
    for right, down in [map(int, (x, y)) for x, y in slopes]:
        col, trees = 0, 0
        rows = PUZZLE.input.splitlines()
        for row in rows[down::down]:
            col += right
            if row[col % len(row)] == '#':
                trees += 1
        answer = answer * trees
    return answer


if __name__ == "__main__":
    PUZZLE.report_a(count_trees('31'))
    PUZZLE.report_b(count_trees('11', '31', '51', '71', '12'))
