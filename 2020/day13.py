#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/13
"""
import collections
import aoc

PUZZLE = aoc.Puzzle(day=13, year=2020)


def solve():
    """Solve puzzle"""
    lines = PUZZLE.input.splitlines()
    start = int(lines[0])
    fleet = collections.OrderedDict()
    offset = 0
    for bus in lines[1].split(','):
        if bus != 'x':
            fleet[offset] = int(bus)
        offset += 1

    next_bus = min(fleet.values(), key=lambda x: x - start % x)
    PUZZLE.report_a(next_bus * (next_bus - start % next_bus))

    time = 0
    inc = None
    for offset, bus in fleet.items():
        if not inc:
            inc = bus
            continue
        while True:
            time += inc
            if (time + offset) % bus == 0:
                break
        inc = inc * bus
    PUZZLE.report_b(time)


if __name__ == "__main__":
    solve()
