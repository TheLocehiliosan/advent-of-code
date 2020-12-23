#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/23
"""
from collections import deque
from itertools import islice
import aoc

PUZZLE = aoc.Puzzle(day=23, year=2020)


class Cup():
    """Linked cups"""
    # pylint: disable=too-few-public-methods
    def __init__(self, label):
        self.label = label
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.label)

    def __repr__(self):
        return f'Cup {self.label} ({str(self.prev)} <-> {str(self.next)})'


def solve_a():
    """Solve part A"""
    # set up cups
    circle = deque(map(int, PUZZLE.input))
    # perform moves
    for _ in range(100):
        # extract three cups
        cur = circle.popleft()
        three = circle.popleft(), circle.popleft(), circle.popleft()

        # find the destination cup
        idx = None
        dest = cur - 1
        while idx is None:
            try:
                idx = circle.index(dest)
                idx += 1
            except ValueError:
                dest -= 1
                if dest < 1:
                    dest = 9
        for item in reversed(three):
            circle.insert(idx, item)

        # put the current cup back
        circle.append(cur)

    # report the answer
    while circle[0] != 1:
        circle.rotate()
    return ''.join(map(str, islice(circle, 1, len(circle))))


def solve_b():
    """Solve part B"""
    # set up cups
    total_cups = 1_000_000
    cups = dict()
    cur = None
    prev_cup = None
    for label in map(int, PUZZLE.input):
        cup = Cup(label)
        if cur is None:
            cur = cup
        cups[label] = cup
        if prev_cup is not None:
            prev_cup.next = cup
            cup.prev = prev_cup
        prev_cup = cup
    label = max(cups)
    while len(cups) < total_cups:
        label += 1
        cup = Cup(label)
        cups[label] = cup
        if prev_cup is not None:
            prev_cup.next = cup
            cup.prev = prev_cup
        prev_cup = cup
    prev_cup.next = cur
    cur.prev = prev_cup

    # perform moves
    for _ in range(10_000_000):
        # extract three cups, and close the circle
        cup1 = cur.next
        cup2 = cup1.next
        cup3 = cup2.next
        cur.next = cup3.next
        cur.next.prev = cur

        # find the destination cup
        dest = cur.label - 1
        if dest == 0:
            dest = total_cups
        while dest in (_.label for _ in [cup1, cup2, cup3]):
            dest -= 1
            if dest == 0:
                dest = total_cups
        dest = cups[dest]

        # link the three cups after the destination
        cup3.next = dest.next
        cup3.next.prev = cup3
        dest.next = cup1
        cup1.prev = dest

        # start on the next cup
        cur = cur.next

    # report the answer
    return cups[1].next.label * cups[1].next.next.label


if __name__ == "__main__":
    PUZZLE.report_a(solve_a())
    PUZZLE.report_b(solve_b())
