import argparse
import csv


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
