import argparse
import csv


def is_non_empty_string(input_string) -> bool:

    # Strip white spaces from the input string
    trimmed_string = input_string.strip()

    # Check if the length of the trimmed string is greater than 0
    return len(trimmed_string) > 0


class Validator:
    def __init__(self, path):
        with open(path, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            self.rows = [row for row in reader]
            self.fields = reader.fieldnames

    def validate(self):
        pass


def main():
    # read csv path from command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", help="Path to the csv file")
    args = parser.parse_args()

    # create instance of validator
    validator = Validator(args.csv_path)
    validator.validate()


if __name__ == "__main__":
    main()
