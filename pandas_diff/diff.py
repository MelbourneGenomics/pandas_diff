import pandas as pd
from oset import oset


def difference(self: pd.DataFrame, other: pd.DataFrame, arrow: str = '→'):
    # Find a set of all columns
    a_cols = oset(self.columns)
    b_cols = oset(other.columns)
    columns = a_cols | b_cols

    # We'll use a and b as the DFs
    a = self
    b = other

    # Ensure all DFs have the same columns for better diffing
    for column in columns:
        for df in (a, b):
            if not column in df:
                df[column] = ''

    # Join the two data frames and produce a multi-indexed data frame
    merged = pd.concat([self, other], keys=['a', 'b'], axis=1)

    # Create the output DF
    result = pd.DataFrame(index=self.index)

    # Now diff every pair of columns
    for column in columns:
        # First, make a series which shows a→b
        diff = merged.a[column].fillna('').astype(str).str.cat(others=merged.b[column].fillna('').astype(str),
                                                               sep=arrow)

        # Now use that series whenever the two series differ (and aren't NAN).
        result[column] = diff.where(
            cond=(merged.a[column] != merged.b[column]) & ~ (pd.isnull(merged.a[column]) & pd.isnull(merged.b[column])),
            other=pd.np.nan
        )

    # Now filter out any row that is all NAN
    result = result[result.notnull().any(axis=1)]

    # Then filter out any column that is all NAN
    result = result.loc[:, result.notnull().any(axis=0)]

    return result


def diff_series(a: pd.Series, b: pd.Series):
    out = a.copy().astype(object)
    for (index, item_a), item_b in zip(a.astype(str).iteritems(), b.astype(str)):
        if item_a == item_b:
            out[index] = ''
        else:
            out[index] = '{} → {}'.format(item_a, item_b)

            # out[index] = list([diff for diff in difflib.ndiff([item_a], [item_b]) if not diff.startswith(' ')])
    return out
