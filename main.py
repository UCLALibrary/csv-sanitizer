import argparse
import csv
from datetime import datetime
import re


def is_non_empty_string(input_string) -> bool:

    # Strip white spaces from the input string
    trimmed_string = input_string.strip()

    # Check if the length of the trimmed string is greater than 0
    return len(trimmed_string) > 0


def datetime_valid(dt_str):
    # case date range
    if "/" in dt_str:
        dates = dt_str.split("/")
        # There should be exactly two dates
        if len(dates) != 2:
            return False

        # Validate each date
        for date in dates:
            try:
                datetime.fromisoformat(date)
            except ValueError:
                return False

        return True

    # case single date
    else:
        # ISO 8601 duration regex pattern
        pattern = r"^P(?=\d|T\d)(?:(\d+)Y)?(?:(\d+)M)?(?:(\d+)D)?(?:T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+(?:\.\d+)?)S)?)?$"
        match = re.match(pattern, dt_str)
        if match is not None:
            return True

        try:
            datetime.fromisoformat(dt_str)
        except:
            return False
        return True


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
