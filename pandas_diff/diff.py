import pandas as pd
from oset import oset


def difference(df_a: pd.DataFrame,
               df_b: pd.DataFrame,
               arrow: str = '→',
               missing_column="<missing column>",
               empty="<empty>",
               show_empty_cols=False,
               show_empty_rows=False,
               renamed={}
               ) -> pd.DataFrame:
    """
    Diffs two data frames by joining them on their indices and returning a DataFrame with cells that show how the two differ

    :param df_a: The initial/first DataFrame, the one that we consider the second as diverging from
    :param df_b: The second DataFrame, one which we consider as diverging from df_a
    :param arrow: The character used to indicate a change in value, e.g. "initial value" + arrow + "final value"
    :param missing_column: The string value used to indicate a column that has been inserted or deleted
    :param empty: The string value used to indicate an empty cell
    :param show_empty_cols: True if every column of the input DataFrames should be printed, even if they are identical
        between DataFrames. Otherwise, ignore such columns
    :param show_empty_rows: True if every row of the input DataFrames should be printed, even if they are identical
        between DataFrames. Otherwise, ignore such rows
    :param renamed: A dictionary showing how columns have been renamed from df_a to df_b. These renamed columns will then
        mapped with each other for the diff. The keys of this dictionary should be the column names in df_a, and the values
        should be the column names in df_b
    :return: A DataFrame, with the same columns as the input DataFrames, but with each cell showing how the two input
        DataFrames differed.
    """

    # We'll use a and b as the DFs
    a = df_a
    b = df_b

    # Rename the columns if needed
    if renamed:
        a.rename(columns=renamed, inplace=True)

    # Find a set of all columns
    a_cols = oset(df_a.columns)
    b_cols = oset(df_b.columns)
    columns = a_cols | b_cols

    # Ensure all DFs have the same columns for better diffing
    for column in columns:
        for df in (a, b):
            if not column in df:
                df[column] = missing_column

    # Join the two data frames and produce a multi-indexed data frame
    merged = pd.concat([a, b], keys=['a', 'b'], axis=1)

    # Create the output DF
    result = pd.DataFrame(index=a.index)

    # Now diff every pair of columns
    for column in columns:
        # First, make a series which shows a→b
        diff = merged.a[column].fillna(empty).astype(str).str.cat(others=merged.b[column].fillna(empty).astype(str),
                                                                  sep=arrow)

        # Now use that series whenever the two series differ (and aren't NAN).
        result[column] = diff.where(
            cond=(merged.a[column] != merged.b[column]) & ~ (pd.isnull(merged.a[column]) & pd.isnull(merged.b[column])),
            other=pd.np.nan
        )

    # Now filter out any row that is all NAN
    if not show_empty_rows:
        result = result[result.notnull().any(axis=1)]

    # Then filter out any column that is all NAN
    if not show_empty_cols:
        result = result.loc[:, result.notnull().any(axis=0)]

    return result
