# Pandas Diff
## Installation
Just run 
```bash
pip install git+https://github.com/MelbourneGenomics/pandas_diff
```

## Command-line Interface
Pandas Diff exposes the `pdiff` command:
```
usage: pdiff [-h] [-d DELIM] [-i INDEX] [-a ARROW] [-e EMPTY] [-l DELETION]
             [-o OUTPUT]
             a b

Diffs two CSV files by joining on their index

positional arguments:
  a                     Input CSV a
  b                     Input CSV b

optional arguments:
  -h, --help            show this help message and exit
  -d DELIM, --delim DELIM
                        The field to use as a delimiter for csvs. Defaults to
                        "," (comma)
  -i INDEX, --index INDEX
                        A list of comma separated columns that will be used as
                        the index for both CSVs
  -a ARROW, --arrow ARROW
                        A string used to separate new and old CSV data.
                        Defaults to " → "
  -e EMPTY, --empty EMPTY
                        A string used to indicate data cells that contain no
                        data. Defaults to "<empty>".
  -l DELETION, --deletion DELETION
                        A string used to indicate a value when the column is
                        deleted. Defaults to "<nocol>".
  -o OUTPUT, --output OUTPUT
                        A file to output to

```
 
Run `pdiff --help` for up-to-date information.

## Python Interface
The main Python entry point is the `difference` function inside `pandas_diff.diff`. You can use it as an input to the
`pipe` function as follows:
```python
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
```

