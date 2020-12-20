#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/20
"""
import math
import operator
import functools
import re
import aoc

PUZZLE = aoc.Puzzle(day=20, year=2020)
MONSTER = [r'..................#.',
           r'#....##....##....###',
           r'.#..#..#..#..#..#...']


class Tile():
    """A tile"""

    def __init__(self, src):
        self.num = int(re.split(r' |:', src)[1])
        self.data = list()
        for line in src.splitlines()[1:]:
            self.data.append(list(line))
        self.sides = self._find_sides()

    def _find_sides(self):
        sides = [self.top, self.bottom, self.left, self.right]
        self.flip()
        self.rotate()
        self.rotate()
        self.rotate()
        sides += [self.top, self.bottom, self.left, self.right]
        return sides

    def __str__(self):
        return f'Tile:{self.num}'

    def __repr__(self):
        rep = f'tile:{self.num}'
        for row in self.data:
            rep += f'\n{" ".join(row)}'
        return rep

    def rotate(self):
        """Rotate clockwise"""
        new = list()
        for row in list(zip(*self.data[::-1])):
            new.append(list(row))
        self.data = new

    def flip(self):
        """Flip"""
        self.data = list(reversed(self.data))

    @property
    def top(self):
        """Top Edge"""
        return ''.join(self.data[0])

    @property
    def bottom(self):
        """Bottom Edge"""
        return ''.join(self.data[-1])

    @property
    def left(self):
        """Left Edge"""
        return ''.join(row[0] for row in self.data)

    @property
    def right(self):
        """Right Edge"""
        return ''.join(row[-1] for row in self.data)

    def position_corner(self, unique):
        """Orient upper left corner"""
        while (self.left not in unique) or (self.top not in unique):
            self.rotate()

    def move_left(self, edge):
        """Orient left side == edge"""
        rotations = 0
        while self.left != edge:
            if rotations == 4:
                self.flip()
                rotations = 0
            else:
                self.rotate()
                rotations += 1

    def move_top(self, edge):
        """Orient top side == edge"""
        rotations = 0
        while self.top != edge:
            if rotations == 4:
                self.flip()
                rotations = 0
            else:
                self.rotate()
                rotations += 1


def solve():
    """Solve part A"""
    tiles = list()
    for tile in PUZZLE.input.split('\n\n'):
        tiles.append(Tile(tile))
    corners = set()
    a_corner = None
    for tile in tiles:
        unique_sides = set()
        other_sides = set()
        for other in tiles:
            if other == tile:
                continue
            other_sides.update(other.sides)
        for side in tile.sides:
            if side not in other_sides:
                unique_sides.add(side)
        if len(unique_sides) == 4:
            corners.add(tile.num)
            a_corner = [tile, unique_sides]
    print(corners)
    PUZZLE.report_a(functools.reduce(operator.mul, corners))
    arrangement = arrange_tiles(tiles, *a_corner)
    image = stitch(arrangement)
    mon = monsters(image)
    rot = 0
    while mon == 0:
        if rot == 4:
            image = flip_image(image)
            rot = 0
        else:
            image = rotate_image(image)
            rot += 1
        mon = monsters(image)
    print(f'moncount:{mon}')
    PUZZLE.report_b(image.count('#') - (mon * 15))


def monsters(image):
    """count monsters"""
    count = 0
    mon_h = len(MONSTER)
    mon_w = len(MONSTER[0])
    rows = image.splitlines()
    for idx, row in enumerate(rows[:-mon_h+1]):
        for col in range(0, len(row)-mon_w):
            if ((re.match(MONSTER[0], str(rows[idx+0][col:col+mon_w+1])))
                    and
                    (re.match(MONSTER[1], str(rows[idx+1][col:col+mon_w+1])))
                    and
                    (re.match(MONSTER[2], str(rows[idx+2][col:col+mon_w+1])))):
                count += 1
    return count


def next_right(tiles, edge):
    """Return next tile on right"""
    for tile in tiles:
        if edge in tile.sides:
            tile.move_left(edge)
            return tile
    return None


def next_below(tiles, edge):
    """Return next tile below"""
    for tile in tiles:
        if edge in tile.sides:
            tile.move_top(edge)
            return tile
    return None


def arrange_tiles(tiles, start, unique_sides):
    """Solve Part B"""
    full_size = int(math.sqrt(len(tiles)))
    start.position_corner(unique_sides)
    row = list([start])
    tiles.remove(start)
    for idx in range(1, full_size):
        next_tile = next_right(tiles, row[idx-1].right)
        row.append(next_tile)
        tiles.remove(next_tile)
    image = list([row])
    for y in range(1, full_size):
        start = next_below(tiles, image[y-1][0].bottom)
        row = list([start])
        tiles.remove(start)
        for x in range(1, full_size):
            next_tile = next_right(tiles, row[x-1].right)
            row.append(next_tile)
            tiles.remove(next_tile)
        image.append(row)
    return image


def stitch(tiles):
    """stitch image together"""
    image = ''
    for row in tiles:
        for index in range(1, 9):
            for tile in row:
                image += ''.join(tile.data[index][1:-1])
            image += '\n'
    return image


def flip_image(image):
    """flip"""
    return '\n'.join(reversed(image.splitlines()))


def rotate_image(image):
    """rotate"""
    data = list()
    for line in image.splitlines():
        data.append(line)
    new = list()
    for row in list(zip(*data[::-1])):
        new.append(list(row))
    image = ''
    for row in new:
        image += ''.join(row) + '\n'
    return image


if __name__ == "__main__":
    solve()
