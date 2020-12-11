#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/11
"""
import collections
import aoc

PUZZLE = aoc.Puzzle(day=11, year=2020)


def look_around(col, row, seats, dirs):
    """Look in all directions"""
    neighbors = 0
    for col_delta, row_delta in dirs:
        spot_col, spot_row = col, row
        searching = True
        while searching:
            spot_col += col_delta
            spot_row += row_delta
            spot = (spot_col, spot_row)
            if spot in seats:
                if seats[spot] == '#':
                    neighbors += 1
                if seats[spot] != '.':
                    searching = False
            else:
                searching = False
    return neighbors


def show_seats(seats):
    """Display seats"""
    print()
    for row in range(10):
        print(''.join([str(seats[(col, row)]) for col in range(10)]))
    print()


def sit(seats, part='a'):
    """Sit down"""
    people = 4 if part == 'a' else 5
    orig = seats.copy()
    new = collections.defaultdict(int)
    for col, row in orig:
        if part == 'a':
            spots = [
                    (col-1, row-1), (col, row-1), (col+1, row-1),
                    (col-1, row),                 (col+1, row),
                    (col-1, row+1), (col, row+1), (col+1, row+1),
                    ]
            neighbors = [seats[_] for _ in spots].count('#')
        else:
            dirs = [
                    (-1, -1), (0, -1), (+1, -1),
                    (-1, 0),           (+1, 0),
                    (-1, +1), (0, +1), (+1, +1),
                    ]
            neighbors = look_around(col, row, seats, dirs)
        if seats[(col, row)] == 'L' and neighbors == 0:
            new[(col, row)] = '#'
        elif seats[(col, row)] == '#' and neighbors >= people:
            new[(col, row)] = 'L'
        else:
            new[(col, row)] = seats[(col, row)]
    return new


def solve(part='a'):
    """Solve puzzle"""
    seats = collections.defaultdict(int)
    for row, line in enumerate(PUZZLE.input.splitlines()):
        for col, char in enumerate(line):
            seats[(col, row)] = char
    while True:
        prev = seats.copy()
        seats = sit(seats, part)
        if seats == prev:
            # show_seats(seats)
            return collections.Counter(seats.values())['#']


if __name__ == "__main__":
    PUZZLE.report_a(solve('a'))
    PUZZLE.report_b(solve('b'))
