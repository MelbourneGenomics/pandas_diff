
Pandas Diff
***********

Contents:


Installation
============

.. code:: bash

   pip install git+https://github.com/MelbourneGenomics/pandas_diff


Command-line Interface
======================

Pandas Diff exposes the ``pdiff`` command:


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
show_empty_cols=True, show_empty_rows=True) ->
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

   :Returns:
      A DataFrame, with the same columns as the input DataFrames, but
      with each cell showing how the two input DataFrames differed.
