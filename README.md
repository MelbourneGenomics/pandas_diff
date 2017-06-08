# Pandas Diff
## Installation
Just run 
```bash
pip install git+https://github.com/MelbourneGenomics/pandas_diff
```

## Command-line Interface
Pandas Diff exposes the `pdiff` command:
```
usage: pdiff [-h] [-d DELIM] [-i INDEX] [-o OUTPUT] a b

Diffs two CSV files by joining on their index

positional arguments:
  a                     Input CSV a
  b                     Input CSV b

optional arguments:
  -h, --help            show this help message and exit
  -d DELIM, --delim DELIM
                        The field to use as a delimiter for csvs
  -i INDEX, --index INDEX
                        A list of comma separated columns that will be used as
                        the index for both CSVs
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

