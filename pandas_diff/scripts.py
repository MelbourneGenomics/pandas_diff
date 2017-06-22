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


def comma_dictionary(input: str):
    return {key: value for column in input.split(',') for key, value in column.split(':')}


def get_parser():
    parser = argparse.ArgumentParser(description='Diffs two CSV files by joining on their index')
    for csv in ('a', 'b'):
        # The positional argument for the CSV itself
        parser.add_argument(csv, type=argparse.FileType(), help='Input CSV {}'.format(csv))

    parser.add_argument('-d', '--delim', help='The field to use as a delimiter for csvs. Defaults to "," (comma)',
                        default=',', required=False)
    parser.add_argument('-i', '--index', type=comma_separated,
                        help='A list of comma separated columns that will be used as the index for both CSVs. '
                             'These are the columns that will be used to join the two CSVs, so make sure you choose the right column.')
    parser.add_argument('-a', '--arrow', help='A string used to separate new and old CSV data. Defaults to " → "',
                        required=False, default=' → ')
    parser.add_argument('-e', '--empty',
                        help='A string used to indicate data cells that contain no data. Defaults to "<empty>".',
                        required=False, default='<empty>')
    parser.add_argument('-l', '--deletion',
                        help='A string used to indicate a value when the column is deleted. Defaults to "<nocol>".',
                        required=False, default='<nocol>')
    parser.add_argument('-r', '--rename',
                        help='A series of comma separated strings of the form "original:renamed", where original is the'
                             'name of the column in CSV a, and renamed is the new name of the column in CSV b',
                        required=False, type=comma_dictionary)
    parser.add_argument('--no-hide-cols', help="Show columns that have no changes in them", action='store_true',
                        default=False, required=False)
    parser.add_argument('--no-hide-rows', help="Show rows that have no changes in them", action='store_true',
                        default=False, required=False)
    parser.add_argument('--hide-index', help="Don't print the index rows (specified with --index) in the output",
                        action='store_true',
                        default=False, required=False)
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()

    # Read the CSVs
    a = pd.read_csv(args.a, delimiter=args.delim)
    b = pd.read_csv(args.b, delimiter=args.delim)

    # Set the index
    if args.index is not None:
        a = a.set_index(keys=args.index)
        b = b.set_index(keys=args.index)

    result = a.pipe(difference, b, arrow=args.arrow, empty=args.empty, missing_column=args.deletion,
                    hide_empty_cols=args.no_hide_cols, hide_empty_rows=args.no_hide_rows, renamed=args.renamed)

    if args.output:
        result.to_csv(args.output, na_rep='', index=not args.hide_index)
    else:
        print(result.to_string(na_rep='', index=not args.hide_index))


if __name__ == '__main__':
    main()
