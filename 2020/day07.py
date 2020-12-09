#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/7
"""
import re
import aoc

PUZZLE = aoc.Puzzle(day=7, year=2020)


def parse_rules():
    """Parse rules into a dictionary"""
    rules = {}
    for line in PUZZLE.input.splitlines():
        (container, contents) = re.split(r' bags contain ', line)
        rules.setdefault(container, list())
        for item in re.split(r'bags?[,.]', contents):
            if item and 'other' not in item:
                count, bag = re.findall(r'^(\d+) (.+)$', item.strip())[0]
                rules[container].extend([bag] * int(count))
    return rules


def find_containers(target, rules):
    """Find all possible containers of target"""
    containers = set()
    for bag in rules:
        if target in rules[bag]:
            containers.update([bag])
            containers.update(find_containers(bag, rules))
    return containers


def count_bags(target, rules):
    """Count total number of bags (inclusive)"""
    count = 1
    for bag in rules[target]:
        count += count_bags(bag, rules)
    return count


def solve():
    """Solve puzzle"""
    target = 'shiny gold'
    rules = parse_rules()
    PUZZLE.report_a(len(find_containers(target, rules)))
    PUZZLE.report_b(count_bags(target, rules) - 1)


if __name__ == "__main__":
    solve()
