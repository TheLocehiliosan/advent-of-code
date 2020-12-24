#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/24
"""
import collections
import re
import aoc

PUZZLE = aoc.Puzzle(day=24, year=2020)
CARDINAL = r'(se|sw|nw|ne|e|w)'
VECTORS = {
        'se': (0, -1, 1),
        'sw': (-1, 0, 1),
        'w': (-1, 1, 0),
        'nw': (0, 1, -1),
        'ne': (1, 0, -1),
        'e': (1, -1, 0),
        }


def adjacent(loc, tiles):
    """Return count of black adjacent tiles"""
    total = 0
    for direction in VECTORS.values():
        adj = tuple(x + y for x, y in zip(direction, loc))
        total += tiles[adj]
    return total


def solve():
    """Solve puzzle"""
    tiles = collections.defaultdict(bool)
    for line in PUZZLE.input.splitlines():
        loc = (0, 0, 0)
        for path in re.findall(CARDINAL, line):
            loc = tuple(x + y for x, y in zip(VECTORS[path], loc))
        tiles[loc] = not tiles[loc]
    PUZZLE.report_a(sum(tiles.values()))

    for tile in tiles.copy():  # expand the existing tiles
        adjacent(tile, tiles)
    for _ in range(100):
        flip = list()
        for tile in tiles.copy():
            if tiles[tile]:
                if adjacent(tile, tiles) not in [1, 2]:
                    flip.append(tile)
            else:
                if adjacent(tile, tiles) == 2:
                    flip.append(tile)
        for tile in flip:
            tiles[tile] = not tiles[tile]
    PUZZLE.report_b(sum(tiles.values()))


if __name__ == "__main__":
    solve()
