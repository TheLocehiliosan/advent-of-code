#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/22
"""
from collections import deque
from itertools import islice
import aoc

PUZZLE = aoc.Puzzle(day=22, year=2020)


def play_rc(deck1, deck2):
    """Play Recursive Combat"""
    seen = set()
    while deck1 and deck2:
        combo = (tuple(deck1), tuple(deck2))
        if combo in seen:
            return 'one', deck1
        seen.add(combo)
        one, two = deck1.popleft(), deck2.popleft()
        if len(deck1) >= one and len(deck2) >= two:
            _one = deque(islice(deck1, 0, one))
            _two = deque(islice(deck2, 0, two))
            winner, *_ = play_rc(_one, _two)
            if winner == 'one':
                deck1.extend([one, two])
            else:
                deck2.extend([two, one])
        else:
            if one > two:
                deck1.extend([one, two])
            else:
                deck2.extend([two, one])
    if deck1:
        return 'one', deck1
    return 'two', deck2


def solve():
    """Solve puzzle"""
    pile1, pile2 = PUZZLE.input.split('\n\n')
    deck1 = deque(map(int, pile1.splitlines()[1:]))
    deck2 = deque(map(int, pile2.splitlines()[1:]))
    while deck1 and deck2:
        one, two = deck1.popleft(), deck2.popleft()
        if one > two:
            deck1.extend([one, two])
        else:
            deck2.extend([two, one])
    deck = deck1 if deck1 else deck2
    PUZZLE.report_a(
        sum((idx * card for idx, card in enumerate(reversed(deck), start=1))))

    deck1 = deque(map(int, pile1.splitlines()[1:]))
    deck2 = deque(map(int, pile2.splitlines()[1:]))
    _, deck = play_rc(deck1, deck2)
    PUZZLE.report_b(
        sum((idx * card for idx, card in enumerate(reversed(deck), start=1))))


if __name__ == "__main__":
    solve()
