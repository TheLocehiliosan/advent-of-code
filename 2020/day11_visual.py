#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/11
"""
import collections
import sys
import aoc
import pygame
import pygame.locals

PUZZLE = aoc.Puzzle(day=11, year=2020)

pygame.init()
pygame.display.set_caption(PUZZLE.puzzle.title)
FPS = pygame.time.Clock()
FPS.tick(60)
SCALE = 10

BLACK = pygame.Color(0, 0, 0)
GREEN = pygame.Color(0, 255, 0)
RED = pygame.Color(255, 0, 0)
WHITE = pygame.Color(255, 255, 255)


def look_around(col, row, seats, dirs):
    """Look in all directions"""
    neighbors = 0
    for col_delta, row_delta in dirs:
        spot_col, spot_row = col, row
        searching = True
        while searching:
            spot_col += col_delta
            spot_row += row_delta
            spot = (spot_col, spot_row)
            if spot in seats:
                if seats[spot] == '#':
                    neighbors += 1
                if seats[spot] != '.':
                    searching = False
            else:
                searching = False
    return neighbors


def show_seats(seats):
    """Display seats"""
    print()
    for row in range(10):
        print(''.join([str(seats[(col, row)]) for col in range(10)]))
    print()


def sit(seats, part='a'):
    """Sit down"""
    people = 4 if part == 'a' else 5
    new = collections.defaultdict(int)
    for col, row in list(seats):
        if part == 'a':
            spots = [
                    (col-1, row-1), (col, row-1), (col+1, row-1),
                    (col-1, row),                 (col+1, row),
                    (col-1, row+1), (col, row+1), (col+1, row+1),
                    ]
            neighbors = [seats[_] for _ in spots].count('#')
        else:
            dirs = [
                    (-1, -1), (0, -1), (+1, -1),
                    (-1, 0),           (+1, 0),
                    (-1, +1), (0, +1), (+1, +1),
                    ]
            neighbors = look_around(col, row, seats, dirs)
        if seats[(col, row)] == 'L' and neighbors == 0:
            new[(col, row)] = '#'
        elif seats[(col, row)] == '#' and neighbors >= people:
            new[(col, row)] = 'L'
        else:
            new[(col, row)] = seats[(col, row)]
    return new


def draw(seats, surf):
    """Draw seats"""
    (width, height) = map(lambda x: x // SCALE, surf.get_size())
    for col in range(width):
        for row in range(height):
            color = BLACK
            if seats[(col, row)] == '#':
                color = RED
            elif seats[(col, row)] == 'L':
                color = GREEN
            pygame.draw.rect(surf, color, (col*SCALE, row*SCALE, SCALE, SCALE))


def wait_for_key():
    """Pause until a key is pressed"""
    while True:
        for ievent in pygame.event.get():
            if ievent.type == pygame.locals.KEYDOWN:
                return
            if ievent.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()


def solve(part='a'):
    """Solve puzzle"""
    seats = collections.defaultdict(int)
    size = (0, 0)
    for row, line in enumerate(PUZZLE.input.splitlines()):
        for col, char in enumerate(line):
            seats[(col, row)] = char
            size = (col * SCALE, row * SCALE)
    surf = pygame.display.set_mode(size)
    surf.fill(BLACK)
    pygame.display.update()
    draw(seats, surf)
    wait_for_key()
    while True:
        prev = seats.copy()
        seats = sit(seats, part)
        draw(seats, surf)
        if seats == prev:
            return collections.Counter(seats.values())['#']
        pygame.display.update()
        for ievent in pygame.event.get():
            if ievent.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    while True:
        PUZZLE.report_a(solve('a'))
        PUZZLE.report_b(solve('b'))
