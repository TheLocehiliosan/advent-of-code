#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/25
"""
import aoc

PUZZLE = aoc.Puzzle(day=25, year=2020)
SUBJECT = 7
SECRET = 20201227


def find_loop(public):
    """Find loop size"""
    count, value = 0, 1
    while True:
        count += 1
        value = value * SUBJECT
        value = value % SECRET
        if value == public:
            return count


def find_private(public, loop_size):
    """Find private key"""
    value = 1
    for _ in range(loop_size):
        value = value * public
        value = value % SECRET
    return value


def solve():
    """Solve puzzle"""
    (card_pub, door_pub) = map(int, PUZZLE.input.splitlines())
    card_loop = find_loop(card_pub)
    key = find_private(door_pub, card_loop)
    PUZZLE.report_a(key)
    PUZZLE.report_b()


if __name__ == "__main__":
    solve()
