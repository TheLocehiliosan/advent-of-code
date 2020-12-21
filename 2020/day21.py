#!/usr/bin/env python3
"""
https://advent opcode.com/2020/day/21
"""
import collections
import re
import aoc

PUZZLE = aoc.Puzzle(day=21, year=2020)


def solve():
    """Solve puzzle"""
    foods = list()
    allergy = collections.defaultdict(list)
    for match in re.findall(r'(.+) \(contains (.+)\)\n?', PUZZLE.input):
        (ingredients, allergens) = match
        ingredients = ingredients.split(' ')
        foods.extend(ingredients)
        for allergen in allergens.split(', '):
            allergy[allergen].extend(ingredients)
    known = dict()
    for allergen in allergy:
        most = max(allergy[allergen].count(x) for x in allergy[allergen])
        allergy[allergen] = {x for x in allergy[allergen]
                             if allergy[allergen].count(x) == most}
    while allergy:
        for allergen in sorted(
                allergy,
                key=lambda i: len([x for x in allergy[i]
                                   if x not in known.values()])):
            unknown = [x for x in allergy[allergen] if x not in known.values()]
            if len(unknown) == 1:
                known[allergen] = unknown[0]
                del allergy[allergen]
    PUZZLE.report_a(sum([1 for food in foods if food not in known.values()]))
    PUZZLE.report_b(','.join([known[_] for _ in sorted(known)]))


if __name__ == "__main__":
    solve()
