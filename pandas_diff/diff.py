import pandas as pd
from oset import oset


def difference(df_a: pd.DataFrame,
               df_b: pd.DataFrame,
               arrow: str = '→',
               missing_column="<missing column>",
               empty="<empty>",
               same='',
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
    :param same: What value to show when two cells have the same value. Defaults to '', an empty string. Can also be
        any arbitrary string, or, if it's the string 'value', instead just show what that value is.
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
    merged = pd.concat([a, b], keys=['a', 'b'], join='inner', axis=1)

    # Group the merged data
    groups = merged.groupby(level=1, axis=1)

    # A DF showing the diff values (A->B) in each cell
    diff = groups.apply(lambda group:
                        group.iloc[:, 0].fillna(empty).astype(str).str.cat(
                            others=group.iloc[:, 1].fillna(empty).astype(str),
                            sep=arrow)
                        )

    # A df with cells that are True where the two cells are different and False otherwise
    mask = groups.apply(lambda group: group.iloc[:, 0] != group.iloc[:, 1])

    # The output is A->B if they're different, otherwise NAN
    result = diff.where(cond=mask, other=pd.np.nan)

    # Now filter out any row that is all NAN
    if not show_empty_rows:
        result = result[result.notnull().any(axis=1)]

    # Then filter out any column that is all NAN
    if not show_empty_cols:
        result = result.loc[:, result.notnull().any(axis=0)]

    if same == 'value':
        # If the user wants to see the values of the cells that are the same, take them from DF a
        result = result.fillna(a)
    else:
        # Otherwise, just fill those cells with the provided values
        result = result.fillna(same)

    return result
