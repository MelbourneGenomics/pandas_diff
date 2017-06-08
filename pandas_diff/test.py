import unittest
import pandas as pd
from pandas_diff.diff import difference


class Tests(unittest.TestCase):
    def test_basic(self):
        a = pd.DataFrame(dict(
            one=["Lorem", "ipsum", "dolor", 'sit', 'amet', 'consectetur', 'adipiscing', 'elit'],
            two=[1, 3, 5, 7, 9, 11, 13, 15]
        ))

        b = pd.DataFrame(dict(
            one=["Loem", "ipsum", "dolor", 'sit', 'amt', 'consectetur', 'adipiscing', 'elit'],
            two=[1, 3, 2, 7, 9, 11, 13, 15],
        ))

        diff = a.pipe(difference, b)
        self.assertEqual(len(diff), 3)

    def test_index(self):
        a = pd.DataFrame(dict(
            one=["Lorem", "ipsum", "dolor", 'sit', 'amet', 'consectetur', 'adipiscing', 'elit'],
            two=[1, 3, 5, 7, 9, 11, 13, 15]
        ), index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

        b = pd.DataFrame(dict(
            one=["Loem", "ipsum", "dolor", 'sit', 'amt', 'consectetur', 'adipiscing', 'elit'],
            two=[1, 3, 2, 7, 9, 11, 13, 15],
        ), index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

        diff = a.pipe(difference, b)
        self.assertEqual(len(diff), 3)

