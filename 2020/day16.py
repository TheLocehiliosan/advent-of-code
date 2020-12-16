#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/16
"""
import collections
import re
import aoc

PUZZLE = aoc.Puzzle(day=16, year=2020)


def parse_input():
    """Parse puzzle input"""
    fields, mine, nearby = PUZZLE.input.split('\n\n')
    match = re.findall(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)\n?', fields)
    rules = dict()
    for field, *bounds in match:
        rules[field] = (
                list(range(int(bounds[0]), int(bounds[1])+1)) +
                list(range(int(bounds[2]), int(bounds[3])+1)))
    my_ticket = list(map(int, mine.splitlines()[1].split(',')))
    tickets = [list(map(int, _.split(','))) for _ in nearby.splitlines()[1:]]
    return rules, my_ticket, tickets


def solve():
    """Solve puzzle"""
    # parse data
    rules, my_ticket, tickets = parse_input()

    # eliminate invalid tickets, noting the error rate
    error_rate = 0
    valid = list()
    for ticket in tickets:
        invalid = False
        for num in ticket:
            if not any(num in scope for scope in rules.values()):
                invalid = True
                error_rate += num
        if not invalid:
            valid.append(ticket)
    PUZZLE.report_a(error_rate)

    # determine which fields are possible for each index
    possible = collections.defaultdict(set)
    for index in range(len(rules)):
        for field, scope in rules.items():
            if all(ticket[index] in scope for ticket in valid):
                possible[field].add(index)

    # determine official fields
    departures = 1
    official = dict()
    for field in sorted(possible, key=lambda i: len(possible[i])):
        for index in possible[field]:
            if index not in official.values():
                official[field] = index
                if 'depart' in field:
                    departures = departures * my_ticket[index]
    PUZZLE.report_b(departures)


if __name__ == "__main__":
    solve()
