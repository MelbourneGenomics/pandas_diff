import unittest
import pandas as pd
from pandas_diff.diff import difference


class Tests(unittest.TestCase):
    a = pd.DataFrame(dict(
        one=["Lorem", "ipsum", "dolor", 'sit', 'amet', 'consectetur', 'adipiscing', 'elit'],
        two=[1, 3, 5, 7, 9, 11, 13, 15]
    ))

    b = pd.DataFrame(dict(
        one=["Loem", "ipsum", "dolor", 'sit', 'amt', 'consectetur', 'adipiscing', 'elit'],
        two=[1, 3, 2, 7, 9, 11, 13, 15],
        three=[True, True, True, True, True, True, True, True]
    ))

    def test_basic(self):
        return self.a.pipe(difference, self.b)
