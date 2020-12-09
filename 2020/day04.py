#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/4
"""
import re
import aoc

PUZZLE = aoc.Puzzle(day=4, year=2020)

FIELDS = {
        'byr': lambda v: 1920 <= int(v) <= 2002,
        'iyr': lambda v: 2010 <= int(v) <= 2020,
        'eyr': lambda v: 2020 <= int(v) <= 2030,
        'hgt': lambda v: v and test_height(v),
        'hcl': lambda v: re.match(r'#[a-f0-9]{6}$', v),
        'ecl': lambda v: v in 'amb blu brn gry grn hzl oth'.split(' '),
        'pid': lambda v: re.match(r'\d{9}$', v),
        }


def parse_passports():
    """Generate dictionary for every passport"""
    for lines in PUZZLE.input.split('\n\n'):
        passport = {}
        for text in lines.split():
            key, value = text.split(':')
            passport[key] = value
        yield passport


def test_height(hgt):
    """Test height"""
    bounds = {
            'cm': {'start': 150, 'end': 193},
            'in': {'start': 59, 'end': 76},
            }
    match = re.match(r'(\d+)(cm|in)$', hgt)
    if match:
        height, kind = match.groups()
        if bounds[kind]['start'] <= int(height) <= bounds[kind]['end']:
            return True
    return False


def solve():
    """Solve puzzle"""
    valid_a, valid_b = 0, 0
    for passport in parse_passports():
        if all(req in passport.keys() for req in FIELDS):
            valid_a += 1
            tests = [test(passport[field]) for field, test in FIELDS.items()]
            if all(tests):
                valid_b += 1
    PUZZLE.report_a(valid_a)
    PUZZLE.report_b(valid_b)


if __name__ == "__main__":
    solve()
