#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/8
"""
import aoc

PUZZLE = aoc.Puzzle(day=8, year=2020)


def solve(part):
    """Solve puzzle"""
    source = PUZZLE.input.splitlines()
    for index, line in enumerate(source):
        pgm = source.copy()
        if part == 'b':
            line = line.translate(str.maketrans('nojm', 'jmno'))
        pgm[index] = line
        acc, counter, seen = 0, 0, set()
        while True:
            if counter == len(pgm):
                return acc
            if counter in seen:
                if part == 'a':
                    return acc
                break
            seen.add(counter)
            inst, param = pgm[counter].split()
            acc += int(param) if inst == 'acc' else 0
            counter += int(param) if inst == 'jmp' else 1


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
