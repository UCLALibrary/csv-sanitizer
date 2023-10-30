import argparse

parser = argparse.ArgumentParser()
parser.add_argument("sample", help="Print out the contents of CLI argument")
args = parser.parse_args()
print(args.sample)