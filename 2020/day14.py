#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/14
"""
import re
import aoc

PUZZLE = aoc.Puzzle(day=14, year=2020)


def create_multi_mask(mask):
    """Create all possible masks from floating 'X' bits"""
    masks = list()
    count = mask.count('X')
    for value in range(2**count):
        binary = bin(value)[2:].zfill(count)
        newmask = re.sub('[01]', '_', mask)
        for digit in binary:
            newmask = newmask.replace('X', digit, 1)
        zeros = int(re.sub('_', '1', newmask), 2)
        ones = int(re.sub('_', '0', newmask), 2)
        masks.append((zeros, ones))
    return masks


def solve():
    """Solve puzzle"""
    ones, zeros = 0, 2**35
    memory_a, memory_b = dict(), dict()
    multi_mask = list()
    for line in PUZZLE.input.splitlines():
        mask = re.findall(r'mask = ([X10]+)', line)
        if mask:
            zeros = int(re.sub('X', '1', mask[0]), 2)
            ones = int(re.sub('X', '0', mask[0]), 2)
            multi_mask = create_multi_mask(mask[0])
            continue
        match = re.findall(r'mem\[(\d+)\] = (\d+)', line)
        if match:
            addr, value = map(int, match[0])
            memory_a[addr] = (value & zeros) | ones
            for mask in multi_mask:
                target_addr = ((addr | ones) & mask[0]) | mask[1]
                memory_b[target_addr] = value

    PUZZLE.report_a(sum(memory_a.values()))
    PUZZLE.report_b(sum(memory_b.values()))


if __name__ == "__main__":
    solve()
