import argparse

parser = argparse.ArgumentParser(description='Renames selected functions')
parser.add_argument('functions', metavar='names', type=str, nargs='+',
                    help='List of function names,')

parser.add_argument('files', metavar='files', type=str, nargs='+',
                    help='python script name ')



args = parser.parse_args()
print(args)