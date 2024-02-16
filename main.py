import argparse
import csv
from datetime import datetime
import re
import os
from pathlib import Path
from os import access, R_OK


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


def file_exists(row, rowNum, errors):
    file_name = row["File Name"]

    file_path = Path(file_name)

    # Path/File exists
    if not file_path.exists() and not file_path.is_file():
        errors.append(f"File {file_path} does not exist ({rowNum})")
        return False

    # Check if file is readable
    if not access(file_path, R_OK):
        errors.append(f"File {file_path} is not readable ({rowNum})")
        return False

    # Check size of file
    if file_path.stat().st_size == 0:
        errors.append(f"File {file_path} is zero bytes ({rowNum})")
        return False

    return True


class Validator:
    def __init__(self, path: str, dir_stub: str = None):

        # Optional directory stub to file location (e.g. /root/to/file-folder/ )
        # If dir_stub is None set to empty string
        self.dir_stub = dir_stub if dir_stub else ""

        _, self.file_extension = os.path.splitext(path)
        with open(path, "r", newline="") as csvfile:

            reader = csv.DictReader(csvfile)
            self.rows = [row for row in reader]
            self.fields = reader.fieldnames
            self.validheaders = [
                "item ark",
                "parent ark",
                "item status id",
                "item status",
                "object type",
                "file name",
                "item sequence",
                "duplicate",
                "delete in title",
                "thumbnail",
                "viewinghint",
                "text direction",
                "visibility",
                "iiif range",
                "type.typeofresource",
                "type.genre",
                "rights.copyrightstatus",
                "rights.statementlocal",
                "rights.servicescontact",
                "language",
                "coverage.geographic",
                "coverage.temporal",
                "subject",
                "alt id.local",
                "title",
                "name.creator",
                "alttitle.uniform",
                "relation.ispartof",
                "summary",
                "description.note",
                "date.creation",
                "date.normalized",
                "publisher.placeoforigin",
                "publisher.publishername",
                "name.subject",
                "name.photographer",
                "name.repository",
                "finding aid url",
                "opac url",
                "bucketeer state",
                "iiif access url",
                "iiif manifest url",
                "media.width",
                "media.height",
                "media.duration",
                "media.format",
                "waveform",
                "license",
            ]

    @classmethod
    def is_csv(self, file_ext, row, field, header, errors):
        # Check file extension is .csv
        if file_ext.lower() != ".csv":
            errors.append(
                f"Incorrect file extension ({file_ext}), please specify a .csv"
            )

        # Check if the file is empty
        if not row:
            errors.append("File is empty")
            return 0

        # Check that a header row exists with valid header names
        found_item = 0
        for item in field:
            if item.lower() in header:
                found_item += 1

        if found_item == 0:
            errors.append("No valid header row exists in file")

    # Run methods and return a list of errors that the csv has
    def validate(self):
        errors = []
        Validator.is_csv(
            self.file_extension, self.rows, self.fields, self.validheaders, errors
        )

        for rowNum, row in enumerate(self.rows, 1):
            file_exists(row, rowNum, errors)

        if errors:
            print("Your file contains these errors: ", errors)
        else:
            print("There are no errors in your file!")


def main():
    # read csv path from command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", help="Path to the csv file")
    parser.add_argument(
        "-s",
        "--stub",
        type=str,
        nargs="?",
        help="The directory stub to append to file paths, e.g. /path/to/masters/",
    )
    args = parser.parse_args()

    # create instance of validator
    validator = Validator(args.csv_path, args.stub)
    # validator.validate()


if __name__ == "__main__":
    main()
