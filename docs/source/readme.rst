Pandas Diff
===========

Installation
------------

.. code-block:: bash

  pip install git+https://github.com/MelbourneGenomics/pandas_diff

Command-line Interface
----------------------
Pandas Diff exposes the ``pdiff`` command:

.. argparse::
    :module: pandas_diff.scripts
    :func: get_parser
    :prog: pdiff


Python Interface
----------------
The main Python entry point is the ``difference`` function inside ``pandas_diff.diff``. You can use it as an input to the
``pipe`` function as follows::

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

.. autofunction:: pandas_diff.diff.difference
