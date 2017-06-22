import unittest
import pandas as pd
from pandas_diff.diff import difference
from pandas_diff.scripts import comma_dictionary


class Tests(unittest.TestCase):
    def test_basic(self):
        a = pd.DataFrame(dict(
            one=["Lorem", "ipsum", "dolor", 'sit', 'amet', 'consectetur', 'adipiscing', ''],
            two=[1, 3, 5, 7, 9, 11, 13, 15],
            same=[True, True, True, True, True, True, True, True]
        ))

        b = pd.DataFrame(dict(
            one=["Loem", "ipsum", "dolor", 'sit', 'amt', 'consectetur', 'adipiscing', 'elit'],
            two=[1, 3, 2, 7, 9, 11, 13, 15],
            same=[True, True, True, True, True, True, True, True]
        ))

        diff = a.pipe(difference, b)

        # The column 'same' should be removed since it's identical, and all but 4 rows should be removed since they're
        # identical. Thus the result should be (4 X 2)
        self.assertEqual(diff.shape, (4, 2))

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

    def test_rename(self):
        """
        Tests the renamed parameter to difference
        """
        a = pd.DataFrame({
            'one': [1, 2, 3, 4, 5],
            'two': [6, 7, 8, 9, 19],
        })

        b = pd.DataFrame({
            'uno': [1, 2, 3, 4, 5],
            'dos': [6, 7, 8, 9, 19],
        })

        diff = a.pipe(difference, b, renamed={'one': 'uno', 'two': 'dos'})
        self.assertEqual(len(diff), 0)

    def test_dict_type(self):
        """
        Tests the comma_dictionary argument type
        """
        parsed = comma_dictionary('one:uno,two:dos')
        self.assertEqual(parsed, {'one': 'uno', 'two': 'dos'})
