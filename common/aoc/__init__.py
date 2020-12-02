# -*- coding: utf-8 -*-
"""aoc common code"""
import argparse
import aocd


class Puzzle():
    """Puzzle utiltiy object"""
    args = None

    def __init__(self, day, year):
        self.day = day
        self.year = year
        self.puzzle = aocd.models.Puzzle(day=day, year=year)
        Puzzle.parse_args()

    @property
    def input(self):
        """Puzzle input"""
        return self.puzzle.input_data

    def report_answer(self, part, answer=None):
        """Report answer to AOC"""
        print(f'Answer {part.upper()}: {answer}')
        if answer is None:
            return
        if Puzzle.args.submit:
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
    def parse_args(cls):
        """Parse command line arguments"""
        if cls.args:
            return
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-s", "--submit",
            help="Submit answers to adventofcode.com",
            action="store_true",
            )
        cls.args = parser.parse_args()
