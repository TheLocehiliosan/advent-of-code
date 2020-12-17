#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/17
"""
import collections
import itertools
import aoc

PUZZLE = aoc.Puzzle(day=17, year=2020)


def count_active_neighbors(pos, space):
    """Generate neighboring positions"""
    active = 0
    dims = len(pos)
    zero = tuple(0 for _ in range(dims))
    for vector in itertools.product(range(-1, 2), repeat=dims):
        if vector != zero:
            active += space[tuple(x + y for x, y in zip(pos, vector))]
    return active


def update(space):
    """Update space"""
    # expand space before updating...
    for pos in list(space):
        count_active_neighbors(pos, space)

    # now update
    future = space.copy()
    for pos in future:
        neighbors = count_active_neighbors(pos, space)
        if future[pos]:
            if neighbors not in [2, 3]:
                future[pos] = 0
        else:
            if neighbors == 3:
                future[pos] = 1
    return future


def solve():
    """Solve puzzle"""
    space_a = collections.defaultdict(int)
    space_b = space_a.copy()
    for y, line in enumerate(PUZZLE.input.splitlines()):
        for x, char in enumerate(line):
            space_a[(x, y, 0)] = 1 if char == '#' else 0
            space_b[(x, y, 0, 0)] = 1 if char == '#' else 0

    for _ in range(6):
        space_a = update(space_a)
    PUZZLE.report_a(sum(space_a.values()))

    for _ in range(6):
        space_b = update(space_b)
    PUZZLE.report_b(sum(space_b.values()))


if __name__ == "__main__":
    solve()
