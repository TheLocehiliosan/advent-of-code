# -*- coding: utf-8 -*-
"""Puzzle related utilities/objects"""
import argparse
import time
import aocd


class Puzzle():
    """Puzzle utility object"""
    _args = None

    def __init__(self, day, year):
        self.start = time.perf_counter()
        self.end_a = None
        self.end_b = None
        self.day = day
        self.year = year
        self.puzzle = aocd.models.Puzzle(day=day, year=year)
        Puzzle._parse_args()

    @property
    def input(self):
        """Puzzle input"""
        return self.puzzle.input_data

    @property
    def sample(self):
        """Fetch some sample data, not the standard input"""
        with open('sample') as data:
            return data.read()

    @property
    def timing(self):
        """Timing report"""
        return '{0:.2f} seconds'.format(self.end_b - self.start)

    def report_stats(self):
        """Report Stats"""
        try:
            print(f'YEAR:{self.year} DAY:{self.day}')
            print(f'Part A: {self.puzzle.my_stats["a"]["time"]}')
            print(f'Part B: {self.puzzle.my_stats["b"]["time"]}')
        except aocd.exceptions.PuzzleUnsolvedError:
            pass

    def report_answer(self, part, answer=None):
        """Report answer to AOC"""
        if part == 'a' and Puzzle._args.decorate:
            self.end_a = time.perf_counter()
            title = f'Day {self.day}: {self.puzzle.title}'
            print(title)
            print('-'*len(title))
        print(f'Answer {part.upper()}: {answer}')
        if part == 'b' and Puzzle._args.decorate:
            self.end_b = time.perf_counter()
            print(self.timing)
            print('')
        if answer is None:
            return
        if Puzzle._args.submit:
            aocd.submit(
                answer,
                part=part,
                day=self.day,
                year=self.year)

    def report_a(self, answer=None):
        """Report answer A"""
        self.report_answer('a', answer)

    def report_b(self, answer=None):
        """Report answer B"""
        self.report_answer('b', answer)

    @classmethod
    def _parse_args(cls):
        """Parse command line arguments"""
        if cls._args:
            return
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-d", "--decorate",
            help="Decorate with a title and spacing",
            action="store_true",
            )
        parser.add_argument(
            "-s", "--submit",
            help="Submit answers to adventofcode.com",
            action="store_true",
            )
        cls._args = parser.parse_args()
