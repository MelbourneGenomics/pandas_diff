from pandas_diff.diff import difference
import argparse
from pathlib import Path
import pandas as pd


def existing_path(input: str):
    path = Path(input)
    if path.exists():
        return path
    else:
        raise argparse.ArgumentTypeError('"{}" is not a valid path and existing path'.format(input))


def comma_separated(input: str):
    return input.split(',')

def get_args():
    parser = argparse.ArgumentParser(description='Diffs two CSV files by joining on their index')
    for csv in ('a', 'b'):
        # The positional argument for the CSV itself
        parser.add_argument(csv, type=argparse.FileType(), help='Input CSV {}'.format(csv))

    parser.add_argument('-d', '--delim', help='The field to use as a delimiter for csvs', default=',', required=False)
    parser.add_argument('-i', '--index', type=comma_separated,
                        help='A list of comma separated columns that will be used as the index for both CSVs')

    parser.add_argument('-a', '--arrow', help='A string used to separate new and old CSVs', required=False)
    parser.add_argument('-o', '--output', help='A file to output to', required=False)
    return parser.parse_args()

def main():
    args = get_args()

    # Read the CSVs
    a = pd.read_csv(args.a, delimiter=args.delim)
    b = pd.read_csv(args.b, delimiter=args.delim)

    # Set the index
    if args.index is not None:
        a = a.set_index(keys=args.index)
        b = b.set_index(keys=args.index)

    result = a.pipe(difference, b)

    if args.output:
        result.to_csv(args.output)
    else:
        print(result.to_string())


if __name__ == '__main__':
    main()
