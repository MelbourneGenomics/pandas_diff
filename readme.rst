
Pandas Diff
***********


Installation
============

.. code:: bash

   pip install git+https://github.com/MelbourneGenomics/pandas_diff


Command-line Interface
======================

Pandas Diff exposes the ``pdiff`` command:

Diffs two CSV files by joining on their index

::

   usage: pdiff [-h] [-d DELIM] [-i INDEX] [-a ARROW] [-e EMPTY] [-l DELETION]
                [-r RENAME] [--no-hide-cols] [--no-hide-rows] [--hide-index]
                a b


Positional Arguments
--------------------

a

Input CSV a

b

Input CSV b


Named Arguments
---------------

-d, --delim

The field to use as a delimiter for csvs. Defaults to “,” (comma)

Default: “,”

-i, --index

A list of comma separated columns that will be used as the index for
both CSVs. These are the columns that will be used to join the two
CSVs, so make sure you choose the right column.

-a, --arrow

A string used to separate new and old CSV data. Defaults to ” → “

Default: ” → “

-e, --empty

A string used to indicate data cells that contain no data. Defaults to
“<empty>”.

Default: “<empty>”

-l, --deletion

A string used to indicate a value when the column is deleted. Defaults
to “<nocol>”.

Default: “<nocol>”

-r, --rename

A series of comma separated strings of the form “original:renamed”,
where original is thename of the column in CSV a, and renamed is the
new name of the column in CSV b

--no-hide-cols

Show columns that have no changes in them

Default: False

--no-hide-rows

Show rows that have no changes in them

Default: False

--hide-index

Don’t print the index rows (specified with –index) in the output

Default: False


Python Interface
================

The main Python entry point is the ``difference`` function inside
``pandas_diff.diff``. You can use it as an input to the ``pipe``
function as follows:

::

   import pandas as pd
   from pandas_diff.diff import difference

   a = pd.DataFrame(dict(
     one=["Lorem", "ipsum", "dolor", 'sit', 'amet', 'consectetur', 'adipiscing', 'elit'],
     two=[1, 3, 5, 7, 9, 11, 13, 15]
   ))

   b = pd.DataFrame(dict(
     one=["Loem", "ipsum", "dolor", 'sit', 'amt', 'consectetur', 'adipiscing', 'elit'],
     two=[1, 3, 2, 7, 9, 11, 13, 15],
     three=[True, True, True, True, True, True, True, True]
   ))

   diff = a.pipe(difference, b)

The full API of the ``difference`` function is as follows:

**pandas_diff.diff.difference(df_a: pandas.core.frame.DataFrame, df_b:
pandas.core.frame.DataFrame, arrow: str = ‘→’,
missing_column=’<missing column>’, empty=’<empty>’,
show_empty_cols=False, show_empty_rows=False, renamed={}) ->
pandas.core.frame.DataFrame**

   Diffs two data frames by joining them on their indices and
   returning a DataFrame with cells that show how the two differ

   :Parameters:
      * **df_a** – The initial/first DataFrame, the one that we
         consider the second as diverging from

      * **df_b** – The second DataFrame, one which we consider as
         diverging from df_a

      * **arrow** – The character used to indicate a change in value,
         e.g. “initial value” + arrow + “final value”

      * **missing_column** – The string value used to indicate a
         column that has been inserted or deleted

      * **empty** – The string value used to indicate an empty cell

      * **show_empty_cols** – True if every column of the input
         DataFrames should be printed, even if they are identical
         between DataFrames. Otherwise, ignore such columns

      * **show_empty_rows** – True if every row of the input
         DataFrames should be printed, even if they are identical
         between DataFrames. Otherwise, ignore such rows

      * **renamed** – A dictionary showing how columns have been
         renamed from df_a to df_b. These renamed columns will then
         mapped with each other for the diff. The keys of this
         dictionary should be the column names in df_a, and the values
         should be the column names in df_b

   :Returns:
      A DataFrame, with the same columns as the input DataFrames, but
      with each cell showing how the two input DataFrames differed.
